import tkinter as tk
import math

def taylor(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    return 1 - result

def z_function(x, b):
    if x == 0:
        return 1 + b
    else:
        return (math.sin(x) / x) + b

b = float(input("Enter the value for b: "))

root = tk.Tk()
root.title("Graphs")

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

for i in range(0, 400):
    x = (i - 200) / 20
    y = taylor(x, 10) * 50
    canvas.create_oval(i, 200 - y, i, 200 - y, fill="blue")

for i in range(0, 400):
    x = (i - 200) / 20
    y = z_function(x, b) * 50
    canvas.create_oval(i, 200 - y, i, 200 - y, fill="red")

root.mainloop()
