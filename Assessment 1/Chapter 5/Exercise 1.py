import tkinter as tk

class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
#details of the dogs
    def description(self):
        return f"Name: {self.name}, Age: {self.age}, Breed: {self.breed}"
    #figuring out who is the older dog
    @classmethod
    def old_dog_woof(cls, dog1st, dog2nd):
        old_dog = dog1st if dog1st.age > dog2nd.age else dog2nd
        print(f"{old_dog.name} says: Woof!")

#creating two dog objects and assigning data to their attributes
dog1st = Dog("Browny", 5, "Chihuahua")
dog2nd = Dog("Wilson", 7, "German Shepherd")

#the data for each dog
print("Dog 1:", dog1st.description())
print("Dog 2:", dog2nd.description())

#method to make the oldest dog "woof"
Dog.old_dog_woof(dog1st, dog2nd)

#simple Tkinter GUI to display dog information
root = tk.Tk()
root.title("Dog Information")

dog1st_label = tk.Label(root, text=dog1st.description())
dog1st_label.pack()

dog2nd_label = tk.Label(root, text=dog2nd.description())
dog2nd_label.pack()

root.mainloop()
