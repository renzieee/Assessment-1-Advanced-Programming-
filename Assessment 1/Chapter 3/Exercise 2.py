import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
#functions for coffee orders
def order_coffee():
    selected_coffee = coffee_var.get()
    options = []

    if milk_var.get():
        options.append("Milk")

    if sugar_var.get():
        options.append("Sugar")

    if chocolate_var.get():
        options.append("Chocolate")

    message = f"You ordered a {selected_coffee} coffee with {', '.join(options)}."
    messagebox.showinfo("Order Confirmation", message)

root = tk.Tk()
root.title("Coffee Vending Machine")
root.geometry("500x500")

#options for coffee
coffee_var = tk.StringVar(value="Espresso")
coffee_label = ttk.Label(root, text="Select Coffee Type:")
coffee_label.pack()

coffee_options = ttk.Combobox(root, textvariable=coffee_var, values=["Espresso", "Spanish Latte", "Cappuccino"])
coffee_options.pack()

#additional of options
sugar_var = tk.BooleanVar(value=False)
milk_var = tk.BooleanVar(value=False)
chocolate_var = tk.BooleanVar(value=False)

check_boxsugars = ttk.Checkbutton(root, text="Sugar", variable=sugar_var)
check_boxsugars.pack()

checkbox_milks = ttk.Checkbutton(root, text="Milk", variable=milk_var)
checkbox_milks.pack()

checkbox_chocolates = ttk.Checkbutton(root, text="Chocolate", variable=chocolate_var)
checkbox_chocolates.pack()

#loading and resizing images
image_espresso = Image.open("espresso.jpg")
image_espresso = image_espresso.resize((200, 100))
photo_espresso = ImageTk.PhotoImage(image_espresso)
label_espresso = ttk.Label(root, image=photo_espresso)
label_espresso.pack()

image_cappucinno = Image.open("capuccino.jpg")
image_cappucinno = image_cappucinno.resize((200, 100))
photo_cappucinno = ImageTk.PhotoImage(image_cappucinno)
label_cappucinno = ttk.Label(root, image=photo_cappucinno)
label_cappucinno.pack()

image_spanishlatte = Image.open("spanish latte.jpg")
image_spanishlatte = image_spanishlatte.resize((200, 100))
spanishlatte = ImageTk.PhotoImage(image_spanishlatte)
label_spanishlatte = ttk.Label(root, image=spanishlatte)
label_spanishlatte.pack()



#order button
order_button = ttk.Button(root, text="Order Coffee", command=order_coffee)
order_button.pack()

root.mainloop()