import tkinter as tk
from tkinter import simpledialog, messagebox

def about_info():
    messagebox.showinfo("About", "Разработчик: \nЯрик Носков, ака: github.com/YaroStrike")

def translate():
    global word, case
    word = simpledialog.askstring("Input word", "Введите слово:")
    case = "UPPERCASE" if var.get() == 0 else "lowercase"
def show_translation():
    messagebox.showinfo("Результат смены регистра", f"Слово: {word}\nПеревод: {word.upper() if var.get() == 0 else word.lower()} ({case})")

root = tk.Tk()
root.geometry("504x180")
root.title("АнтиCapsLock")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu)
menu.add_cascade(label="File |", menu=file_menu)
menu.add_cascade(label="Носков Ярослав Дмитриевич 2ИСП-6, вариант 10")
file_menu.add_command(label="Begin", command=translate)
file_menu.add_command(label="Work", command=show_translation)
file_menu.add_command(label="About", command=about_info)

var = tk.IntVar()
radio_group = tk.Radiobutton(root, text="lowercase", variable=var, value=1)
radio_group.pack()
radio_group = tk.Radiobutton(root, text="UPPERCASE", variable=var, value=0)
radio_group.pack()

root.mainloop()
