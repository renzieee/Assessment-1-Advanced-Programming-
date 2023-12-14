import tkinter as tk
from tkinter import messagebox

class Employee:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.id = 0
        self.salary = 0

    def setData(self, name, age, employee_id, salary):
        self.name = name
        self.age = age
        self.id = employee_id
        self.salary = salary

    def getData(self):
        return self.name, self.age, self.id, self.salary

#function for adding employee details
def add_employee():
    #input values from the entry fields
    name = name_entry.get()
    age = int(age_entry.get())
    employee_id = int(id_entry.get())
    salary = float(salary_entry.get())

    #creating an employee object and set the data
    emp = Employee()
    emp.setData(name, age, employee_id, salary)

    #append the employee data to the employees list
    employees.append(emp)

    #the entry fields for the next input
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    id_entry.delete(0, tk.END)
    salary_entry.delete(0, tk.END)

#display employee details
def display_employee():
    #creating a text box to display the output
    output = tk.Toplevel()
    output.title("Employee Details")

    #create headers for the table
    tk.Label(output, text="Name").grid(row=0, column=0)
    tk.Label(output, text="Position").grid(row=0, column=1)
    tk.Label(output, text="Salary").grid(row=0, column=2)
    tk.Label(output, text="ID").grid(row=0, column=3)

    #displaying employee data in a table format
    for i, emp in enumerate(employees, start=1):
        name, age, employee_id, salary = emp.getData()
        position = "Position" + str(i)
        tk.Label(output, text=name).grid(row=i, column=0)
        tk.Label(output, text=position).grid(row=i, column=1)
        tk.Label(output, text=salary).grid(row=i, column=2)
        tk.Label(output, text=employee_id).grid(row=i, column=3)


root = tk.Tk()
root.title("Employee Details")

#creating empty list to store employee objects
employees = []

#labels and entry fields for user input
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

id_label = tk.Label(root, text="ID:")
id_label.pack()
id_entry = tk.Entry(root)
id_entry.pack()

salary_label = tk.Label(root, text="Salary:")
salary_label.pack()
salary_entry = tk.Entry(root)
salary_entry.pack()

#buttons to add employee details
add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.pack()

#buttons to display employee details
display_button = tk.Button(root, text="Display Employees", command=display_employee)
display_button.pack()

root.mainloop()
