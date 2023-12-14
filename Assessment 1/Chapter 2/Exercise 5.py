import tkinter as tk
from tkinter import messagebox

#function for perform calculations
def calculate():
    try:
        #getting user to input values
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        
        #getting the selected operation
        operation = operation_var.get()

        #addition
        if operation == "Addition":
            result = num1 + num2
            #subtraction
        elif operation == "Subtraction":
            result = num1 - num2
            #multilpication
        elif operation == "Multiplication":
            result = num1 * num2
            #division
        elif operation == "Division":
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed")
                return
            else:
                result = num1 / num2
        elif operation == "Modulo Division":
            if num2 == 0:
                messagebox.showerror("Error", "Modulo division by zero is not allowed")
                return
            else:
                result = num1 % num2
        else:
            result = "Invalid Operation"

        #updating the result label
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

#creating the main window
root = tk.Tk()
root.title("Basic Calculator")

#entry the widgets for numbers
entry1 = tk.Entry(root)
entry1.pack()

entry2 = tk.Entry(root)
entry2.pack()

#dropdown for the operations
operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo Division"]
operation_var = tk.StringVar(root)
operation_var.set(operations[0]) #set the default operation

operation_dropdown = tk.OptionMenu(root, operation_var, *operations)
operation_dropdown.pack()

#the button to calculate
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.pack()

#label for display result
result_label = tk.Label(root, text="Result: ", font=("Arial", 10))
result_label.pack()

#starting the main loop
root.mainloop()
