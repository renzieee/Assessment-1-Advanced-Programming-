import tkinter as tk

def save_to_file():
    name = entry_name.get()
    age = entry_age.get()
    hometown = entry_hometown.get()

    with open("bio.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

def read_from_file():
    with open("bio.txt", "r") as file:
        content = file.read()
        label_output.config(text=content)

# Create main window
root = tk.Tk()
root.title("Bio Information")
root.geometry("500x400")

# Create labels and entry fields
label_name = tk.Label(root, text="Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_age = tk.Label(root, text="Age:")
label_age.pack()

entry_age = tk.Entry(root)
entry_age.pack()

label_hometown = tk.Label(root, text="Hometown:")
label_hometown.pack()

entry_hometown = tk.Entry(root)
entry_hometown.pack()

# Create buttons
button_saves = tk.Button(root, text="Save to your File", command=save_to_file)
button_saves.pack()

button_reads = tk.Button(root, text="Read from your File", command=read_from_file)
button_reads.pack()

# Create label to display output
label_output = tk.Label(root, text="", wraplength=350)
label_output.pack()

# Start the tkinter event loop
root.mainloop() 