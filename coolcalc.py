# Cool calculator

import customtkinter as ctk

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
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, "end")
            entry.insert("end", str(result))
        except:
            entry.delete(0, "end")
            entry.insert("end", "Error")
    elif button_text == "C":
        entry.delete(0, "end")
    else:
        entry.insert("end", button_text)

# Button layout
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

# Create button grid
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10, fill="both", expand=True)

for i in range(4):
    button_frame.columnconfigure(i, weight=1)
for i in range(4):
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