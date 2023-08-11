import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget to display input and results
entry = tk.Entry(window, width=30)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define and create number buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for button in buttons:
    text, row, column = button
    btn = tk.Button(window, text=text, padx=15, pady=10, command=lambda num=text: button_click(num))
    btn.grid(row=row, column=column)

# Create a clear button
clear_btn = tk.Button(window, text="Clear", padx=5, pady=10, command=button_clear)
clear_btn.grid(row=5, column=0, columnspan=2, pady=10)

# Create an equal button
equal_btn = tk.Button(window, text="=", padx=15, pady=10, command=button_equal)
equal_btn.grid(row=5, column=2, columnspan=2, pady=10)

# Run the GUI main loop
window.mainloop()
