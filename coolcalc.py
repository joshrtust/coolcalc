# Cool calculator

import customtkinter as ctk
import ast
import operator as op

# Supported operators
operators = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg
}

def eval_expr(expr):
    """
    Safely evaluate a mathematical expression.
    """
    def _eval(node):
        if isinstance(node, ast.Num):  # <number>
            return node.n
        elif isinstance(node, ast.BinOp):  # <left> <operator> <right>
            return operators[type(node.op)](_eval(node.left), _eval(node.right))
        elif isinstance(node, ast.UnaryOp):  # <operator> <operand> e.g., -1
            return operators[type(node.op)](_eval(node.operand))
        else:
            raise TypeError(node)
    
    return _eval(ast.parse(expr, mode='eval').body)

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("CoolCalc")  # Window title
root.geometry("300x400") # Default window size
root.minsize(300, 400) # Minimum window size

# Create Entry Field
entry = ctk.CTkEntry(root, font=("Arial", 24), width=350, height=50, justify="right")
entry.pack(pady=20)

# Function to handle button clicks
def on_click(button_text):
    if button_text == "=": # Equals
        try:
            expression = entry.get().replace("^", "**")
            result = eval_expr(expression)
            entry.delete(0, "end")
            entry.insert("end", str(result))
        except Exception as e:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    elif button_text == "C": # Clear
        entry.delete(0, "end")
    elif button_text == "B": # Backspace
        entry.delete(len(entry.get()) - 1, "end")
    elif button_text == "+/-":  # Toggle negative sign
        try:
            value = float(entry.get())  # Convert to float
            entry.delete(0, "end")
            entry.insert("end", str(-value))  # Negate the number
        except:
            pass  # Ignore errors (e.g., if the field is empty)
    else:
        entry.insert("end", button_text)

# Button layout
buttons = [
    "C", "B", "^", "/",  
    "7", "8", "9", "*",  
    "4", "5", "6", "-",  
    "1", "2", "3", "+",  
    "+/-", "0", ".", "="
]

# Create button grid
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10, fill="both", expand=True)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(5):
    button_frame.rowconfigure(i, weight=1)

for idx, text in enumerate(buttons):
    btn = ctk.CTkButton(
        button_frame,
        text=text,
        font=("Arial", 20),
        width=80,
        height=80,
        corner_radius=10,  # Rounded button corners
        command=lambda b=text: on_click(b)
    )
    btn.grid(row=idx // 4, column=idx % 4, padx=2, pady=2, sticky="nsew")

root.mainloop()