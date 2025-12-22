import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Linux Style Calculator")
        self.root.geometry("350x450")
        self.root.configure(bg="#2e2e2e")  # Dark gray background

        # Expression storage
        self.expression = ""

        # --- Display Area ---
        self.display_var = tk.StringVar()
        self.display_frame = tk.Frame(self.root, bg="#1e1e1e", bd=5, relief="sunken")
        self.display_frame.pack(pady=20, padx=10, fill="x")

        self.display_label = tk.Label(
            self.display_frame, textvariable=self.display_var, 
            anchor="e", font=("Arial", 24), bg="#1e1e1e", fg="white", 
            padx=10, height=2
        )
        self.display_label.pack(fill="x")

        # --- Button Layout ---
        self.buttons_frame = tk.Frame(self.root, bg="#2e2e2e")
        self.buttons_frame.pack()

        buttons = [
            'C', '%', '/', 'Backspace',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '0', '.', '='
        ]

        # Row and Column management
        row = 0
        col = 0
        for button in buttons:
            btn_text = "Del" if button == "Backspace" else button
            
            # Styling: Gray/Black combinations
            bg_color = "#404040" if button.isdigit() or button == "." else "#1a1a1a"
            fg_color = "white"
            
            action = lambda x=button: self.on_click(x)
            
            # Create the embossed buttons
            b = tk.Button(
                self.buttons_frame, text=btn_text, width=5, height=2,
                font=("Arial", 14, "bold"), bg=bg_color, fg=fg_color,
                relief="raised", bd=3, command=action
            )
            
            # Special case for '=' button width
            if button == "=":
                b.grid(row=row, column=col, columnspan=2, sticky="nsew", padx=2, pady=2)
                col += 1
            else:
                b.grid(row=row, column=col, padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1

        # --- Keyboard Bindings ---
        self.root.bind('<Key>', self.key_input)
        self.root.bind('<Return>', lambda e: self.calculate())
        self.root.bind('<BackSpace>', lambda e: self.backspace())
        self.root.bind('<Escape>', lambda e: self.clear())

    def on_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.clear()
        elif char == "Backspace":
            self.backspace()
        else:
            self.expression += str(char)
            self.display_var.set(self.expression)

    def key_input(self, event):
        key = event.char
        # Allow numbers and operators
        if key in "0123456789+-*/%.":
            self.on_click(key)
        # Handle the '=' key specifically
        elif key == "=":
            self.calculate()

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def calculate(self):
        try:
            # eval() processes the string as math
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except Exception:
            messagebox.showerror("Error", "Invalid Input")
            self.clear()

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()