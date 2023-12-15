import tkinter as tk
from tkinter import ttk
import math
#to calculate and display the area of the circle
def calculate_circle_area2():
    radius1 = float(entry_circle_radius1.get())
    area2 = math.pi * (radius1 ** 2)
    result_circle_label.config(text=f"area of the Circle: {area2:.2f}")

#to calculate and display the area of the square
def calculate_square_area2():
    sides = float(entry_squares_sides.get())
    area2 = sides ** 2
    result_square_label.config(text=f"area of the Square: {area2:.2f}")
#to calculate and display the area of the rectangle
def calculate_rectangle_area2():
    length = float(entry_rectangle_length.get())
    width = float(entry_rectangle_width.get())
    area2 = length * width
    label_rectangle_result.config(text=f"area of the Rectangle: {area2:.2f}")

#main window
root = tk.Tk()
root.title("Area Calculator")
root.geometry("450x350")

#creating a notebook 
notebook = ttk.Notebook(root)

#circle tab
circles_tab = ttk.Frame(notebook)
notebook.add(circles_tab, text="Circle")

label_circle_radius1 = ttk.Label(circles_tab, text="Enter radius1:")
label_circle_radius1.grid(row=0, column=0, padx=7, pady=7)

entry_circle_radius1 = ttk.Entry(circles_tab)
entry_circle_radius1.grid(row=0, column=1, padx=7, pady=7)

button_circle_calculate = ttk.Button(circles_tab, text="Calculate", command=calculate_circle_area2)
button_circle_calculate.grid(row=1, column=0, columnspan=2, pady=10)

result_circle_label = ttk.Label(circles_tab, text="area of the Circle: ")
result_circle_label.grid(row=2, column=0, columnspan=2)

#square tab
square_tab = ttk.Frame(notebook)
notebook.add(square_tab, text="Square")

label_square_sides = ttk.Label(square_tab, text="Enter side length:")
label_square_sides.grid(row=0, column=0, padx=7, pady=7)

entry_squares_sides = ttk.Entry(square_tab)
entry_squares_sides.grid(row=0, column=1, padx=7, pady=7)

button_square_calculate = ttk.Button(square_tab, text="Calculate", command=calculate_square_area2)
button_square_calculate.grid(row=1, column=0, columnspan=2, pady=10)

result_square_label = ttk.Label(square_tab, text="area of the Square: ")
result_square_label.grid(row=2, column=0, columnspan=2)

#rectangle tab
tab_rectangles = ttk.Frame(notebook)
notebook.add(tab_rectangles, text="Rectangle")

label_rectangle_length = ttk.Label(tab_rectangles, text="Enter length:")
label_rectangle_length.grid(row=0, column=0, padx=7, pady=7)

entry_rectangle_length = ttk.Entry(tab_rectangles)
entry_rectangle_length.grid(row=0, column=1, padx=7, pady=7)

label_rectangle_width = ttk.Label(tab_rectangles, text="Enter width:")
label_rectangle_width.grid(row=1, column=0, padx=7, pady=7)

entry_rectangle_width = ttk.Entry(tab_rectangles)
entry_rectangle_width.grid(row=1, column=1, padx=7, pady=7)

button_rectangle_calculate = ttk.Button(tab_rectangles, text="Calculate", command=calculate_rectangle_area2)
button_rectangle_calculate.grid(row=2, column=0, columnspan=2, pady=10)

label_rectangle_result = ttk.Label(tab_rectangles, text="area of the Rectangle: ")
label_rectangle_result.grid(row=3, column=0, columnspan=2)


notebook.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()