import tkinter as tk
from tkinter import messagebox
class Quiz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("test.mpt.ru")
        self.geometry("400x300")
        self.current_question = 0
        self.score = 0
        self.questions = [
            {"вопрос":"Лучшая дистанция спринта?", "варианты":["60m","200m","1km","400m"], "ответ": "60m"},
            {"вопрос":"Лучшая дистанция not-спринта?", "варианты":["60m","200m","1km","400m"], "ответ": "1km"}
        ]
        self.create_widgets()
    def create_widgets(self):
        self.question_label = tk.Label(self, text=self.questions[self.current_question]["вопрос"])
        self.question_label.pack()
        self.input=tk.Entry(self)
        self.input.pack()
        self.options_var=tk.StringVar()
        self.option_radios = []
        for option in self.questions[self.current_question]["варианты"]:
            option_radio = tk.Radiobutton(self, text=option, variable=self.options_var, value=option)
            option_radio.pack()
            self.option_radios.append(option_radio)
        self.submit_button = tk.Button(self, text="Ответить", command=self.check_answer)
        self.submit_button.pack()
    def check_answer(self):
        user_answer = self.input.get()
        selected_answer = self.options_var.get()
        correct_answer = self.questions[self.current_question]["ответ"]
        if selected_answer == correct_answer or user_answer == correct_answer:
            self.score +=1
        self.current_question +=1
        if self.current_question < len(self.questions):
            self.question_label.config(text=self.questions[self.current_question]["вопрос"])
            for i, option in enumerate(self.questions[self.current_question]["варианты"]):
                self.options_var.set("")
                self.option_radios[i].config(text=option)
        else:
            percent = (self.score)/(len(self.questions))*100
            with open("answers.txt", "w") as file:
                file.write(f"{self.question_label}{selected_answer}/n")
            messagebox.showinfo("Тест пройден!", f"Вы правы на {self.score} из {len(self.questions)} вопросов ({round(percent, 2)}%).")
            self.destroy()
if __name__ == "__main__":
    app = Quiz()
    app.mainloop()
