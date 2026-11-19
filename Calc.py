import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Calculator")
window.geometry("400x550")
window.minsize(250, 350)
window.configure(bg="#202124")

for i, weight in enumerate([1, 2, 8, 2]):
    window.grid_rowconfigure(i, weight=weight)

window.grid_columnconfigure(0, weight=1)


def validate_input(value):
    allowed = "0123456789.+-*/"

    if all(char in allowed for char in value):
        return True

    return False


def button_click(value):
    Calc_entry.insert(tk.END, value)


def clear():
    Calc_entry.delete(0, tk.END)


def backspace():
    current = Calc_entry.get()

    if current:
        Calc_entry.delete(len(current) - 1, tk.END)


def calculate():
    try:
        expression = Calc_entry.get()

        if not expression:
            return

        result = eval(expression)

        Calc_entry.delete(0, tk.END)
        Calc_entry.insert(0, str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

    except:
        messagebox.showerror("Error", "Invalid Calculation")


Calc_label = tk.Label(
    window,
    text="Calculator",
    font=("Arial", 18, "bold"),
    bg="#202124",
    fg="white"
)
Calc_label.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

validation = window.register(validate_input)

Calc_entry = tk.Entry(
    window,
    font=("Arial", 22),
    justify="right",
    borderwidth=5,
    validate="key",
    validatecommand=(validation, "%P"),
    bg="Green",
    fg="white",
    insertbackground="white",
    relief="flat"
)
Calc_entry.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

button_frame = tk.Frame(
    window,
    bg="#202124"
)
button_frame.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

for i in range(4):
    button_frame.grid_columnconfigure(i, weight=1)
    button_frame.grid_rowconfigure(i, weight=1)

buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    (".", 3, 0), ("0", 3, 1), ("C", 3, 2), ("+", 3, 3)
]

for text, row, column in buttons:
    command = clear if text == "C" else lambda value=text: button_click(value)

    if text == "C":
        bg_color = "#b3261e"
    elif text in "+-*/":
        bg_color = "#41444b"
    else:
        bg_color = "#303134"

    tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16, "bold"),
        bg=bg_color,
        fg="white",
        activebackground="#5f6368",
        activeforeground="white",
        relief="flat",
        command=command
    ).grid(
        row=row,
        column=column,
        sticky="nsew",
        padx=3,
        pady=3
    )

bottom_frame = tk.Frame(
    window,
    bg="#202124"
)
bottom_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

bottom_frame.grid_columnconfigure(0, weight=1)
bottom_frame.grid_columnconfigure(1, weight=1)
bottom_frame.grid_rowconfigure(0, weight=1)

tk.Button(
    bottom_frame,
    text="⌫",
    font=("Arial", 18, "bold"),
    bg="#41444b",
    fg="white",
    activebackground="#5f6368",
    activeforeground="white",
    relief="flat",
    command=backspace
).grid(
    row=0,
    column=0,
    sticky="nsew",
    padx=3,
    pady=3
)

tk.Button(
    bottom_frame,
    text="=",
    font=("Arial", 18, "bold"),
    bg="#1a73e8",
    fg="white",
    activebackground="#4285f4",
    activeforeground="white",
    relief="flat",
    command=calculate
).grid(
    row=0,
    column=1,
    sticky="nsew",
    padx=3,
    pady=3
)

window.mainloop()