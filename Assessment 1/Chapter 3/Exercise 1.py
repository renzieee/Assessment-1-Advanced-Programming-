import tkinter as tk
from tkinter import ttk

def update_greeting():
    name = entry_name.get()
    color = color_var.get()
    greeting = f"Hello, {name}!"
    label_display.config(text=greeting, foreground=color)

# Create main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("700x450")

# Create InputFrame with blue background
frame_input = ttk.Frame(root, padding=23, style="Input.TFrame")
frame_input.grid(row=0, column=0, padx=23, pady=23)

# Create DisplayFrame with green background
frame_display = ttk.Frame(root, padding=23, style="Display.TFrame", width=250)
frame_display.grid(row=0, column=2, padx=23, pady=23)

# Create a custom style for the frames
style = ttk.Style()

# Style for InputFrame
style.configure("Input.TFrame", background="#87CEFB")

# Style for DisplayFrame
style.configure("Display.TFrame", background="#98FB99")

# Create widgets for InputFrame
label_title = ttk.Label(frame_input, text="Welcome!!!", font=("Helvetica", 25, "bold"), foreground="blue")
label_title.grid(row=0, column=0, columnspan=3, pady=23)

label_name = ttk.Label(frame_input, text="Name:")
label_name.grid(row=2, column=0, sticky="w")

entry_name = ttk.Entry(frame_input)
entry_name.grid(row=2, column=2, pady=6)

label_color = ttk.Label(frame_input, text="Select Color:")
label_color.grid(row=3, column=0, sticky="w")

color_var = tk.StringVar(value="black")
dropdown_color = ttk.Combobox(frame_input, textvariable=color_var, values=["black", "red", "blue", "green"])
dropdown_color.grid(row=3, column=2, pady=6)

button_update = ttk.Button(frame_input, text="Update Greeting", command=update_greeting)
button_update.grid(row=4, column=0, columnspan=3, pady=23)

# Create a label for DisplayFrame
label_display = ttk.Label(frame_display, font=("Helvetica", 25), anchor="center")
label_display.pack(expand=True, fill="both")

root.mainloop()