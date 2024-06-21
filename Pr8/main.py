import tkinter as tk
import math

# тейлор
def taylor_series(x, n):
    result = 0
    for i in range(n):
        result += ((-1)**i) * (x**(2*i)) / math.factorial(2*i)
    return 1 - result

# Function for z(x)
def z_function(x, b):
    if x == 0:
        return 1 + b
    else:
        return (math.sin(x) / x) + b

# Input value for b
b = float(input("Enter the value for b: "))

# Create a Tkinter window
root = tk.Tk()
root.title("Graphs")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Draw y(x) graph
for i in range(0, 400):
    x = (i - 200) / 20
    y = taylor_series(x, 10) * 50
    canvas.create_oval(i, 200 - y, i, 200 - y, fill="blue")

# Draw z(x) graph
for i in range(0, 400):
    x = (i - 200) / 20
    y = z_function(x, b) * 50
    canvas.create_oval(i, 200 - y, i, 200 - y, fill="red")

root.mainloop()
