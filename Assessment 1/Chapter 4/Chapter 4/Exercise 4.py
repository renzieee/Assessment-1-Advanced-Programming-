import tkinter as tk
#counting how many characters are there in sentences.txt
def count_occurrences():
    char = entry.get()
    with open('sentences.txt', 'r') as file:
        content = file.read()
    counts = content.count(char)
    label_result.config(text=f"The characters '{char}' occurs {counts} times.")

#main window
root = tk.Tk()
root.title("Character Occurrence Counter")
root.geometry("400x300")

#creating the label and entry for the characters 
label_char = tk.Label(root, text="Enter the characters:")
label_char.pack(pady=12)
entry = tk.Entry(root)
entry.pack(pady=12)

# button to trigger thee counting
count_buttons = tk.Button(root, text="Count Occurrences", command=count_occurrences)
count_buttons.pack(pady=12)

#creating a label display the results
label_result = tk.Label(root, text="")
label_result.pack()

#starting the tkinter event loop
root.mainloop()