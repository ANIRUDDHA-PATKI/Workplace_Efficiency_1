import tkinter as tk
from tkinter import ttk, messagebox
import math
import re

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("500x700")
        self.root.configure(bg="#2c3e50")
        self.root.resizable(False, False)
        
        # Calculator state
        self.current_expression = ""
        self.memory = 0
        self.angle_mode = "DEG"  # DEG or RAD
        self.inverse_mode = False
        
        # Create main frame
        self.main_frame = tk.Frame(root, bg="#2c3e50")
        self.main_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Create display
        self.create_display()
        
        # Create buttons
        self.create_buttons()
        
        # Bind keyboard events
        self.bind_keyboard_events()
        
    def create_display(self):
        # Display frame
        display_frame = tk.Frame(self.main_frame, bg="#34495e", relief="raised", bd=2)
        display_frame.pack(fill="x", pady=(0, 10))
        
        # Expression display
        self.expression_var = tk.StringVar()
        self.expression_var.set("0")
        self.expression_display = tk.Label(
            display_frame,
            textvariable=self.expression_var,
            font=("Arial", 14),
            bg="#34495e",
            fg="#ecf0f1",
            anchor="e",
            padx=10,
            pady=5
        )
        self.expression_display.pack(fill="x")
        
        # Result display
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=("Arial", 20, "bold"),
            bg="#34495e",
            fg="#2ecc71",
            anchor="e",
            padx=10,
            pady=5
        )
        self.result_display.pack(fill="x")
        
        # Mode indicators
        mode_frame = tk.Frame(display_frame, bg="#34495e")
        mode_frame.pack(fill="x", padx=10, pady=5)
        
        self.mode_label = tk.Label(
            mode_frame,
            text=f"Mode: {self.angle_mode}",
            font=("Arial", 10),
            bg="#34495e",
            fg="#bdc3c7"
        )
        self.mode_label.pack(side="left")
        
        self.inverse_label = tk.Label(
            mode_frame,
            text="",
            font=("Arial", 10),
            bg="#34495e",
            fg="#e74c3c"
        )
        self.inverse_label.pack(side="right")
        
    def create_buttons(self):
        # Button styles
        button_style = {
            "font": ("Arial", 12),
            "relief": "raised",
            "bd": 2,
            "width": 8,
            "height": 2
        }
        
        # Create button frames
        self.create_function_buttons(button_style)
        self.create_number_buttons(button_style)
        self.create_operator_buttons(button_style)
        self.create_scientific_buttons(button_style)
        
    def create_function_buttons(self, style):
        # Function buttons frame
        func_frame = tk.Frame(self.main_frame, bg="#2c3e50")
        func_frame.pack(fill="x", pady=2)
        
        # Clear and memory buttons
        buttons = [
            ("C", "#e74c3c", self.clear),
            ("CE", "#e67e22", self.clear_entry),
            ("⌫", "#f39c12", self.backspace),
            ("MC", "#9b59b6", self.memory_clear),
            ("MR", "#3498db", self.memory_recall),
            ("M+", "#27ae60", self.memory_add),
            ("M-", "#e74c3c", self.memory_subtract)
        ]
        
        for i, (text, color, command) in enumerate(buttons):
            btn = tk.Button(
                func_frame,
                text=text,
                bg=color,
                fg="white",
                command=command,
                **style
            )
            btn.grid(row=0, column=i, padx=2, pady=2, sticky="ew")
            func_frame.columnconfigure(i, weight=1)
            
    def create_number_buttons(self, style):
        # Number buttons frame
        num_frame = tk.Frame(self.main_frame, bg="#2c3e50")
        num_frame.pack(fill="both", expand=True, pady=2)
        
        # Number button layout
        numbers = [
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["0", ".", "±"]
        ]
        
        for i, row in enumerate(numbers):
            for j, num in enumerate(row):
                if num == "±":
                    btn = tk.Button(
                        num_frame,
                        text=num,
                        bg="#95a5a6",
                        fg="white",
                        command=self.negate,
                        **style
                    )
                else:
                    btn = tk.Button(
                        num_frame,
                        text=num,
                        bg="#34495e",
                        fg="white",
                        command=lambda n=num: self.add_to_expression(n),
                        **style
                    )
                btn.grid(row=i, column=j, padx=2, pady=2, sticky="ew")
                num_frame.columnconfigure(j, weight=1)
            num_frame.rowconfigure(i, weight=1)
            
    def create_operator_buttons(self, style):
        # Operator buttons frame
        op_frame = tk.Frame(self.main_frame, bg="#2c3e50")
        op_frame.pack(fill="x", pady=2)
        
        operators = [
            ("+", "#e67e22"),
            ("-", "#e67e22"),
            ("×", "#e67e22"),
            ("÷", "#e67e22"),
            ("=", "#27ae60")
        ]
        
        for i, (op, color) in enumerate(operators):
            if op == "=":
                btn = tk.Button(
                    op_frame,
                    text=op,
                    bg=color,
                    fg="white",
                    command=self.calculate,
                    **style
                )
            else:
                btn = tk.Button(
                    op_frame,
                    text=op,
                    bg=color,
                    fg="white",
                    command=lambda o=op: self.add_operator(o),
                    **style
                )
            btn.grid(row=0, column=i, padx=2, pady=2, sticky="ew")
            op_frame.columnconfigure(i, weight=1)
            
    def create_scientific_buttons(self, style):
        # Scientific buttons frame
        sci_frame = tk.Frame(self.main_frame, bg="#2c3e50")
        sci_frame.pack(fill="x", pady=2)
        
        # Scientific functions organized in rows
        scientific_functions = [
            # Row 1: Trigonometric functions
            [("sin", "#8e44ad", self.sin), ("cos", "#8e44ad", self.cos), ("tan", "#8e44ad", self.tan)],
            # Row 2: Inverse trigonometric functions
            [("asin", "#8e44ad", self.asin), ("acos", "#8e44ad", self.acos), ("atan", "#8e44ad", self.atan)],
            # Row 3: Logarithmic functions
            [("ln", "#2980b9", self.ln), ("log", "#2980b9", self.log), ("log10", "#2980b9", self.log10)],
            # Row 4: Exponential and power functions
            [("e^x", "#16a085", self.exp), ("x^2", "#16a085", self.square), ("x^y", "#16a085", self.power)],
            # Row 5: Other functions
            [("√", "#27ae60", self.sqrt), ("1/x", "#27ae60", self.reciprocal), ("|x|", "#27ae60", self.abs)],
            # Row 6: Constants and mode
            [("π", "#e74c3c", self.pi), ("e", "#e74c3c", self.e), ("DEG/RAD", "#f39c12", self.toggle_angle_mode)],
            # Row 7: Additional functions
            [("n!", "#9b59b6", self.factorial), ("10^x", "#2980b9", self.ten_power), ("2^x", "#2980b9", self.two_power)]
        ]
        
        for i, row in enumerate(scientific_functions):
            for j, (text, color, command) in enumerate(row):
                btn = tk.Button(
                    sci_frame,
                    text=text,
                    bg=color,
                    fg="white",
                    command=command,
                    **style
                )
                btn.grid(row=i, column=j, padx=2, pady=2, sticky="ew")
                sci_frame.columnconfigure(j, weight=1)
            sci_frame.rowconfigure(i, weight=1)
            
    def bind_keyboard_events(self):
        self.root.bind("<Key>", self.handle_keypress)
        self.root.bind("<Return>", lambda event: self.calculate())
        self.root.bind("<Escape>", lambda event: self.clear())
        self.root.bind("<BackSpace>", lambda event: self.backspace())
        
    def handle_keypress(self, event):
        key = event.char
        if key.isdigit() or key == ".":
            self.add_to_expression(key)
        elif key in "+-*/":
            self.add_operator(key)
        elif key == "=":
            self.calculate()
            
    def add_to_expression(self, value):
        if self.current_expression == "0" and value != ".":
            self.current_expression = value
        else:
            self.current_expression += value
        self.update_display()
        
    def add_operator(self, operator):
        if self.current_expression and self.current_expression[-1] not in "+-*/":
            # Convert display operators to Python operators
            if operator == "×":
                operator = "*"
            elif operator == "÷":
                operator = "/"
            self.current_expression += operator
            self.update_display()
            
    def clear(self):
        self.current_expression = ""
        self.update_display()
        
    def clear_entry(self):
        self.current_expression = ""
        self.result_var.set("0")
        
    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        if not self.current_expression:
            self.current_expression = ""
        self.update_display()
        
    def negate(self):
        if self.current_expression:
            if self.current_expression.startswith("-"):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = "-" + self.current_expression
            self.update_display()
            
    def update_display(self):
        if self.current_expression:
            # Convert Python operators back to display operators
            display_expr = self.current_expression.replace("*", "×").replace("/", "÷")
            self.expression_var.set(display_expr)
        else:
            self.expression_var.set("0")
            
    def calculate(self):
        try:
            if not self.current_expression:
                return
                
            # Convert display operators to Python operators
            expr = self.current_expression.replace("×", "*").replace("÷", "/")
            
            # Evaluate the expression
            result = eval(expr)
            
            # Format result
            if isinstance(result, (int, float)):
                if result == int(result):
                    result = int(result)
                else:
                    result = round(result, 10)
                    
            self.result_var.set(str(result))
            self.current_expression = str(result)
            
        except Exception as e:
            messagebox.showerror("Error", f"Invalid expression: {str(e)}")
            self.clear()
            
    # Memory functions
    def memory_clear(self):
        self.memory = 0
        
    def memory_recall(self):
        self.current_expression = str(self.memory)
        self.update_display()
        
    def memory_add(self):
        try:
            self.memory += float(self.result_var.get())
        except:
            pass
            
    def memory_subtract(self):
        try:
            self.memory -= float(self.result_var.get())
        except:
            pass
            
    # Scientific functions
    def sin(self):
        try:
            value = float(self.result_var.get())
            if self.angle_mode == "DEG":
                value = math.radians(value)
            result = math.sin(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def cos(self):
        try:
            value = float(self.result_var.get())
            if self.angle_mode == "DEG":
                value = math.radians(value)
            result = math.cos(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def tan(self):
        try:
            value = float(self.result_var.get())
            if self.angle_mode == "DEG":
                value = math.radians(value)
            result = math.tan(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def asin(self):
        try:
            value = float(self.result_var.get())
            result = math.asin(value)
            if self.angle_mode == "DEG":
                result = math.degrees(result)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def acos(self):
        try:
            value = float(self.result_var.get())
            result = math.acos(value)
            if self.angle_mode == "DEG":
                result = math.degrees(result)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def atan(self):
        try:
            value = float(self.result_var.get())
            result = math.atan(value)
            if self.angle_mode == "DEG":
                result = math.degrees(result)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def ln(self):
        try:
            value = float(self.result_var.get())
            result = math.log(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def log(self):
        try:
            value = float(self.result_var.get())
            result = math.log(value, 2)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def log10(self):
        try:
            value = float(self.result_var.get())
            result = math.log10(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def exp(self):
        try:
            value = float(self.result_var.get())
            result = math.exp(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def square(self):
        try:
            value = float(self.result_var.get())
            result = value ** 2
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def power(self):
        try:
            value = float(self.result_var.get())
            self.current_expression = f"{value}^"
            self.update_display()
        except:
            pass
            
    def sqrt(self):
        try:
            value = float(self.result_var.get())
            result = math.sqrt(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def reciprocal(self):
        try:
            value = float(self.result_var.get())
            result = 1 / value
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def abs(self):
        try:
            value = float(self.result_var.get())
            result = abs(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def pi(self):
        self.current_expression = str(math.pi)
        self.update_display()
        
    def e(self):
        self.current_expression = str(math.e)
        self.update_display()
        
    def toggle_angle_mode(self):
        self.angle_mode = "RAD" if self.angle_mode == "DEG" else "DEG"
        self.mode_label.config(text=f"Mode: {self.angle_mode}")
        
    def factorial(self):
        try:
            value = int(float(self.result_var.get()))
            if value < 0:
                raise ValueError("Factorial not defined for negative numbers")
            result = math.factorial(value)
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def ten_power(self):
        try:
            value = float(self.result_var.get())
            result = 10 ** value
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass
            
    def two_power(self):
        try:
            value = float(self.result_var.get())
            result = 2 ** value
            self.result_var.set(str(result))
            self.current_expression = str(result)
        except:
            pass

def main():
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()