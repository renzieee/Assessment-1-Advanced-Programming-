import tkinter as tk
from tkinter import ttk
#class for the arithmetic operation
class ArithmeticOperations:
    def __init__(self):
        self.result = 0
    #method of performing arithmetic operation
    def calculate(self, operation, num1, num2):
        if operation == "Addition":
            self.result = num1 + num2
        elif operation == "Subtraction":
            self.result = num1 - num2
        elif operation == "Multiplication":
            self.result = num1 * num2
        elif operation == "Division":
            self.result = num1 / num2
#function for performing the calculation based on the user input
def perform_calculation():
    operation = operations_combobox.get()
    num1 = float(entry_n1.get())
    num2 = float(entry_n2.get())

    calculator = ArithmeticOperations()
    calculator.calculate(operation, num1, num2)
    results_label.config(text=f"Result: {calculator.result}")
#creating the main window
root = tk.Tk()
root.title("Arithmetic Operation")
#creating frames for organizing widgets
frames= ttk.Frame(root, padding=13)
frames.grid(row=0, column=0, padx=13, pady=13)
#labels and entry widgets for the numbers and for the operations
operations_label = ttk.Label(frames, text="Operation:")
operations_label.grid(row=0, column=0, padx=7, pady=7)
options_operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operations_combobox = ttk.Combobox(frames, values=options_operations)
operations_combobox.grid(row=0, column=1, padx=7, pady=7)

n1_label = ttk.Label(frames, text="Number 1:")
n1_label.grid(row=1, column=0, padx=7, pady=7)
entry_n1 = ttk.Entry(frames)
entry_n1.grid(row=1, column=1, padx=7, pady=7)

n2_label = ttk.Label(frames, text="Number 2:")
n2_label.grid(row=2, column=0, padx=7, pady=7)
entry_n2 = ttk.Entry(frames)
entry_n2.grid(row=2, column=1, padx=7, pady=7)
#buttons for calculate
buttons_calculates = ttk.Button(frames, text="Calculate", command=perform_calculation)
buttons_calculates.grid(row=3, column=0, columnspan=2, pady=13)
#label for display results
results_label = ttk.Label(frames, text="Results:")
results_label.grid(row=4, column=0, columnspan=2)

root.mainloop()