import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("300x400")

        self.expression = ""

        # 입력창
        self.entry = tk.Entry(root, font=("Arial", 24), justify="right")
        self.entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

        # 버튼 생성
        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
            ['=', ',', 'BMI']
        ]

        for row in buttons:
            frame = tk.Frame(root)
            frame.pack(expand=True, fill="both")
            for char in row:
                btn = tk.Button(
                    frame,
                    text=char,
                    font=("Arial", 18),
                    command=lambda ch=char: self.on_click(ch)
                )
                btn.pack(side="left", expand=True, fill="both")

    def on_click(self, char):
        if char == 'C':
            self.expression = ""
        elif char =='BMI':
            try:
                self.expression = self.bmi_calc(self.expression)
            except Exception:
                self.expression = "입력: 키(cm),몸무게"
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)

    def bmi_calc(self, input):
        
        height, weight = map(float, input.split(','))
        
        if height <= 0 or weight <= 0:
            return "키 몸무게 입력 오류."
        
        height = height / 100
        bmi = weight / ( height ** 2 )
        bmi = round(bmi, 2)

        if bmi < 18.5:
            result = "저체중"
        elif bmi < 23:
            result = "정상"
        elif bmi < 25:
            result = "과제충"
        elif bmi < 30:
            result = "비만"
        else :
            result = "고도비만"

        return f"BMI= {bmi}, {result}"
    