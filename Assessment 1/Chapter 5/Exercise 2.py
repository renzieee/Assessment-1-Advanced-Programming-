import tkinter as tk
from tkinter import messagebox

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def calcGrade(self):
        #calculating the average of the three marks
        return (self.mark1 + self.mark2 + self.mark3) / 3
    
    def display(self):
        #displaying the student name and calculated grade average
        average = self.calcGrade()
        return f"Student Name: {self.name}\nAverage Grade: {average:.2f}"

#creating a students object and display the details
def process_student():
    #getting the input values from the user
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())

    #creating a students object with the input values
    student_obj = Students(name, mark1, mark2, mark3)

    #student details
    result = student_obj.display()
    messagebox.showinfo("Student Details", result)

#creating the main window
root = tk.Tk()
root.title("Student Details")

#labels and entry fields for student details
name_label = tk.Label(root, text="Enter Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

mark1_label = tk.Label(root, text="Enter Mark 1:")
mark1_label.pack()

mark1_entry = tk.Entry(root)
mark1_entry.pack()

mark2_label = tk.Label(root, text="Enter Mark 2:")
mark2_label.pack()

mark2_entry = tk.Entry(root)
mark2_entry.pack()

mark3_label = tk.Label(root, text="Enter Mark 3:")
mark3_label.pack()

mark3_entry = tk.Entry(root)
mark3_entry.pack()

#the button to proceed to the student details
button_process = tk.Button(root, text="Process", command=process_student)
button_process.pack()

root.mainloop()
