import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("계산기")
        self.root.geometry("500x550")

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
            ['=',',', '등수']
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
        elif char == '등수':
            try:
                self.expression = self.rank_calc(self.expression)
                
            except Exception:
                self.expression = "입력 : 점수,평균,표준편차,총 인원"
        elif char == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "에러"
        else:
            self.expression += str(char)

        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.expression)
        
    def rank_calc(self, parts):
        part = list(map(float, parts.split(',')))
        if len(part) != 4:
            return "입력 : 점수,평균,표준편차,총 인원"
        score, mean, stddev, total = part
        if stddev <= 0:
            return "표준편차 는 0보다 큰 수 입니다."
        z = (score - mean) / stddev
        percent = 0.5 * ( 1 + math.erf(z / math.sqrt(2)))
        rank = math.ceil((1 - percent) * total)
        return f"상위 {round(percent*100, 2)}%, 예상 등수 : {rank}등"