import tkinter as tk
from tkinter import ttk
from math import pi

class Shape:
    def __init__(self):
        self.sides = []

    def inputSides(self):
        pass
#getting the radius of circle
class Circle(Shape):
    def inputSides(self):
        radius = float(radius_entry.get())
        self.sides.append(radius)

    def area(self):
        return pi * (self.sides[0] ** 2)
#getting lenghts and widths of rectangle
class Rectangle(Shape):
    def inputSides(self):
        lenghts = float(lenghts_entry.get())
        widths = float(widths_entry.get())
        self.sides.extend([lenghts, widths])

    def area(self):
        return self.sides[0] * self.sides[1]
#getting the base and height of the triangle
class Triangle(Shape):
    def inputSides(self):
        base = float(base_entry.get())
        height = float(height_entry.get())
        self.sides.extend([base, height])

    def area(self):
        return 0.6 * self.sides[0] * self.sides[1]
#function for displaying the area
def calculate_area():
    shape = shapes_combobox.get()
    if shape == "Circle":
        circles = Circle()
        circles.inputSides()
        label_result.config(text=f"Area: {circles.area()} square units")
    elif shape == "Rectangle":
        rectangles = Rectangle()
        rectangles.inputSides()
        label_result.config(text=f"Area: {rectangles.area()} square units")
    elif shape == "Triangle":
        triangles = Triangle()
        triangles.inputSides()
        label_result.config(text=f"Area: {triangles.area()} square units")

root = tk.Tk()
root.title("Shape Area Calculator")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)

shape_label = ttk.Label(frame, text="Select Shape:")
shape_label.grid(row=0, column=0, padx=6, pady=6)

shapes = ["Circle", "Rectangle", "Triangle"]
shapes_combobox = ttk.Combobox(frame, values=shapes, state="readonly")
shapes_combobox.grid(row=0, column=1, padx=6, pady=6)
shapes_combobox.current(0)

buttons_calcuates = ttk.Button(frame, text="Calculate Area", command=calculate_area)
buttons_calcuates.grid(row=1, column=0, columnspan=2, pady=10)

#circle columns and row and its spacing
label_radius = ttk.Label(frame, text="Radius:")
label_radius.grid(row=2, column=0, padx=6, pady=6)
radius_entry = ttk.Entry(frame)
radius_entry.grid(row=2, column=1, padx=6, pady=6)

#rectangle columns and row and its spacing
label_lenghts = ttk.Label(frame, text="Lenght:")
label_lenghts.grid(row=3, column=0, padx=6, pady=6)
lenghts_entry = ttk.Entry(frame)
lenghts_entry.grid(row=3, column=1, padx=6, pady=6)

label_widths = ttk.Label(frame, text="Width:")
label_widths.grid(row=4, column=0, padx=6, pady=6)
widths_entry = ttk.Entry(frame)
widths_entry.grid(row=4, column=1, padx=6, pady=6)

#triangle columns and row and its spacing
label_base = ttk.Label(frame, text="Base:")
label_base.grid(row=6, column=0, padx=6, pady=6)
base_entry = ttk.Entry(frame)
base_entry.grid(row=6, column=1, padx=6, pady=6)

label_height = ttk.Label(frame, text="Height:")
label_height.grid(row=6, column=0, padx=6, pady=6)
height_entry = ttk.Entry(frame)
height_entry.grid(row=6, column=1, padx=6, pady=6)

label_result = ttk.Label(frame, text="Area:")
label_result.grid(row=7, column=0, columnspan=2, pady=(10, 0))

root.mainloop()