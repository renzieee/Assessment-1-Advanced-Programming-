import tkinter as tk
from tkinter import ttk

def update_greeting():
    user_name = entry_name.get()
    selected_color = color_var.get()
    greeting = f"Hello, {user_name}! Have a great day!"
    greeting_label.config(text=greeting, fg=selected_color)

#creating the main window
root = tk.Tk()
root.title("Greetings App")

#creating frames
frame_input = ttk.Frame(root, padding="10")
frame_input.pack(fill=tk.X)

frame_display = ttk.Frame(root, padding="10")
frame_display.pack(fill=tk.X)

#inputing widgets
lable_title = ttk.Label(frame_input, text="Please enter your name:", foreground="blue")
lable_title.pack()

entry_name = ttk.Entry(frame_input)
entry_name.pack()

color_var = tk.StringVar()
color_var.set("green")

option_color = ttk.OptionMenu(frame_input, color_var, "green", "blue", "red", "yellow")
option_color.pack()

button_update = ttk.Button(frame_input, text="Update Greeting", command=update_greeting)
button_update.pack()

#displayframe for widgets
greeting_label = ttk.Label(frame_display, text="", wraplength=200)
greeting_label.pack()

#setting different background colors for each frame
frame_input.config(bg="light blue")
frame_display.config(bg="light green")

root.mainloop()