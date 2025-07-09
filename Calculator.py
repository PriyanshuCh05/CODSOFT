import tkinter as tk
from tkinter import messagebox
import math

def press(key):
    current = entry_var.get()
    
    if key == '√':
        try:
            result = math.sqrt(eval(current))
            entry_var.set(str(result))
        except:
            messagebox.showerror("Error", "Invalid input for square root")
            entry_var.set("")
    elif key == 'log':
        try:
            result = math.log10(eval(current))
            entry_var.set(str(result))
        except:
            messagebox.showerror("Error", "Invalid input for log")
            entry_var.set("")
    elif key == '^':
        entry_var.set(current + '**')  # Power operator
    else:
        entry_var.set(current + str(key))

def clear():
    entry_var.set("")

def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except ZeroDivisionError:
        messagebox.showerror("Error", "Oops! You can't divide by zero.")
        entry_var.set("")
    except:
        messagebox.showerror("Error", "Please enter a valid expression.")
        entry_var.set("")

# GUI Setup (Dark Mode)
root = tk.Tk()
root.title("Calculator")
root.geometry("310x470")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

entry_var = tk.StringVar()

entry = tk.Entry(
    root, textvariable=entry_var,
    font=("Helvetica", 22),
    bd=6, relief="flat",
    justify='right',
    bg="#2d2d2d", fg="white", insertbackground="white"
)
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '^', '+'),
    ('√', 'log', '=', 'C')
]

# Dark mode color palette
btn_bg = "#3c3f41"
btn_fg = "white"
btn_active = "#505357"
equal_bg = "#2e8b57"
clear_bg = "#ff6347"

for row in buttons:
    frame = tk.Frame(root, bg="#1e1e1e")
    frame.pack(expand=True, fill='both')
    for btn_text in row:
        if btn_text == '=':
            tk.Button(frame, text=btn_text, font=("Helvetica", 18),
                      bg=equal_bg, fg="white", activebackground=equal_bg,
                      command=calculate).pack(side="left", expand=True, fill="both", padx=1, pady=1)
        elif btn_text == 'C':
            tk.Button(frame, text=btn_text, font=("Helvetica", 18),
                      bg=clear_bg, fg="white", activebackground=clear_bg,
                      command=clear).pack(side="left", expand=True, fill="both", padx=1, pady=1)
        else:
            tk.Button(frame, text=btn_text, font=("Helvetica", 18),
                      bg=btn_bg, fg=btn_fg, activebackground=btn_active,
                      command=lambda b=btn_text: press(b)).pack(side="left", expand=True, fill="both", padx=1, pady=1)

root.mainloop()
