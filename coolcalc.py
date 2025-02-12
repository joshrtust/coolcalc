# Cool calculator

import tkinter as tk

root = tk.Tk()
root.title("CoolCalc")
root.geometry("300x400")
root.grid_rowconfigure(0, weight=1)  # The entry field will expand in the first row
root.grid_columnconfigure(0, weight=1)  # First column for the entry field

# Entry field for numbers
entry = tk.Entry(root, width=20, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Function to handle button clicks
def on_click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())  # Evaluate the expression
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif button_text == "C":
        entry.delete(0, tk.END)  # Clear input
    else:
        entry.insert(tk.END, button_text)  # Append button text to entry

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Configure rows and columns to expand proportionally
for i in range(1, 5):  # Rows
    root.grid_rowconfigure(i, weight=1)  # Give each row equal weight
for j in range(4):  # Columns
    root.grid_columnconfigure(j, weight=1)  # Give each column equal weight

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, font=("Arial", 15), width=5, height=2,
              command=lambda b=button: on_click(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


root.mainloop()