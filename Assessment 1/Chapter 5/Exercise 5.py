import tkinter as tk
from tkinter import ttk

class Animal:
    def __init__(self, Type, Name, Colour, Age, Weight, Noise):
        self.Type = Type
        self.Name = Name
        self.Colour = Colour
        self.Age = Age
        self.Weight = Weight
        self.Noise = Noise

    def sayHello(self):
        print(f"{self.Name} says hello!")

    def makeNoise(self):
        print(f"{self.Name} makes a {self.Noise} noise!")

    def animalDetails(self):
        details = f"Type: {self.Type}\nName: {self.Name}\nColour: {self.Colour}\nAge: {self.Age}\nWeight: {self.Weight}\nNoise: {self.Noise}"
        return details
#the input values from entry widgets
def create_animal():
    Type = entry_types.get()
    Name = entry_names.get()
    Colour = entry_colours.get()
    Age = int(entry_ages.get())
    Weight = float(entry_weights.get())
    Noise = entry_noises.get()
    #creating a new animal with provided details
    new_animal = Animal(Type, Name, Colour, Age, Weight, Noise)
    new_animal.sayHello()
    new_animal.makeNoise()
    #displaying animal details in the result label
    results_label.config(text=new_animal.animalDetails())
#creating main window
root = tk.Tk()
root.title("Animal Interaction")
root.geometry("350x500")

frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, padx=10, pady=10)
#entry and labels for animal details
type_labels = ttk.Label(frame, text="Type:")
type_labels.grid(row=0, column=0, padx=5, pady=5)
entry_types = ttk.Entry(frame)
entry_types.grid(row=0, column=1, padx=5, pady=5)

names_label = ttk.Label(frame, text="Name:")
names_label.grid(row=1, column=0, padx=5, pady=5)
entry_names = ttk.Entry(frame)
entry_names.grid(row=1, column=1, padx=5, pady=5)

colours_label = ttk.Label(frame, text="Colour:")
colours_label.grid(row=2, column=0, padx=5, pady=5)
entry_colours = ttk.Entry(frame)
entry_colours.grid(row=2, column=1, padx=5, pady=5)

ages_label = ttk.Label(frame, text="Age:")
ages_label.grid(row=3, column=0, padx=5, pady=5)
entry_ages = ttk.Entry(frame)
entry_ages.grid(row=3, column=1, padx=5, pady=5)

weights_label = ttk.Label(frame, text="Weight:")
weights_label.grid(row=4, column=0, padx=5, pady=5)
entry_weights = ttk.Entry(frame)
entry_weights.grid(row=4, column=1, padx=5, pady=5)

noises_label = ttk.Label(frame, text="Noise:")
noises_label.grid(row=5, column=0, padx=5, pady=5)
entry_noises = ttk.Entry(frame)
entry_noises.grid(row=5, column=1, padx=5, pady=5)

create_buttons = ttk.Button(frame, text="Create Animal", command=create_animal)
create_buttons.grid(row=6, column=0, columnspan=2, pady=10)

results_label = ttk.Label(frame, text="")
results_label.grid(row=7, column=0, columnspan=2, pady=(0, 10))

root.mainloop()