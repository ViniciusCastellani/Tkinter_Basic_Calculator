import tkinter as tk
from tkinter import *
from tkinter import messagebox

#--------------------------------
# FUNCTIONS

def add_expression(symbol):
    global expression

    expression += str(symbol)
    equation_label.set(expression)

def equal():
    global expression

    try:
        total = str(eval(expression))
        equation_label.set(total)
    except ZeroDivisionError:
        tk.messagebox.showwarning(title="Error", message="Cannot divide by 0!")
    except SyntaxError:
        tk.messagebox.showwarning(title="Error", message="Invalid operation")

def clear():
    global expression

    expression = ""
    equation_label.set(expression)

#---------------------------
# WINDOW CREATION

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)
window.geometry("400x500")

window.configure(background="black")

#---------------------------
# GLOBAL VARIABLES

expression = ""
equation_label = StringVar()

#--------------------------------
# RESULT LABEL CREATION

result_label = tk.Label(window, textvariable=equation_label, bg="black", fg="white", font=("verdana", 30, "bold"), width=20, height=2)
result_label.pack()

#--------------------------------
# BUTTON FRAME CREATION

frame = tk.Frame(window)
frame.pack()

frame_clear = tk.Frame(window)
frame_clear.pack()

#--------------------------------
# BUTTONS CREATION

button_7 = tk.Button(frame, text="7", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(7))
button_8 = tk.Button(frame, text="8", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(8))
button_9 = tk.Button(frame, text="9", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(9))
button_4 = tk.Button(frame, text="4", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(4))
button_5 = tk.Button(frame, text="5", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(5))
button_6 = tk.Button(frame, text="6", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(6))
button_1 = tk.Button(frame, text="1", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(1))
button_2 = tk.Button(frame, text="2", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(2))
button_3 = tk.Button(frame, text="3", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(3))
button_0 = tk.Button(frame, text="0", width=10, height=5, bg="#DCDCDC", fg="black", font=("verdana", 9), command=lambda: add_expression(0))

button_sum = tk.Button(frame, text="+", width=15, height=5, bg="#A9A9A9", fg="black", font=("verdana", 9), command=lambda: add_expression('+'))
button_multiply = tk.Button(frame, text="X", width=15, height=5, bg="#A9A9A9", fg="black", font=("verdana", 9), command=lambda: add_expression('*'))
button_divide = tk.Button(frame, text="/", width=15, height=5, bg="#A9A9A9", fg="black", font=("verdana", 9), command=lambda: add_expression('/'))
button_subtract = tk.Button(frame, text="-", width=10, height=5, bg="#A9A9A9", fg="black", font=("verdana", 9), command=lambda: add_expression('-'))
button_equals = tk.Button(frame, text="=", bg="#DC143C", fg="black", width=15, height=5, font=("verdana", 9), command=equal)
button_dot = tk.Button(frame, text=".", width=10, height=5, bg="#A9A9A9", fg="black", font=("verdana", 9), command=lambda: add_expression('.'))
button_clear = tk.Button(frame_clear, text="Clear", width=50, height=5, bg="#A9A9A9", fg="black", font=("verdana", 9), command=clear)

#--------------------------------
# BUTTON DISPLAY

button_7.grid(row=0, column=0)
button_8.grid(row=0, column=1)
button_9.grid(row=0, column=2)
button_divide.grid(row=0, column=3)

button_4.grid(row=1, column=0)
button_5.grid(row=1, column=1)
button_6.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

button_1.grid(row=2, column=0)
button_2.grid(row=2, column=1)
button_3.grid(row=2, column=2)
button_sum.grid(row=2, column=3)

button_dot.grid(row=3, column=0)
button_0.grid(row=3, column=1)
button_subtract.grid(row=3, column=2)
button_equals.grid(row=3, column=3)

button_clear.pack()

#--------------------------------

window.mainloop()

