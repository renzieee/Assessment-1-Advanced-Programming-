import tkinter as tk
#using sentences.txt to count how many sentences 
def count_occurrences():
    search_string = entry.get().strip()
    if search_string:
        with open("sentences.txt", "r") as file:
            content = file.read()
            occurrences = content.lower().count(search_string.lower())
            label_results.config(text=f"The string appears {occurrences} times.")
    else:
        label_results.config(text="Please enter a search string.")


root = tk.Tk()
root.title("String Occurrence Counter")
root.geometry("400x300")

#labels and the entry field
label_entry = tk.Label(root, text="Enter the string:")
label_entry.pack()

entry = tk.Entry(root)
entry.pack()

#creating a button
button_counts = tk.Button(root, text="Count the Occurrences", command=count_occurrences)
button_counts.pack()

#label to display the result
label_results = tk.Label(root, text="", wraplength=320)
label_results.pack()


root.mainloop()