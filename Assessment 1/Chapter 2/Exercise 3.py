import tkinter as tk
from tkinter import ttk

#codes to perform login authentication
def on_login():

    #getting username and password from entry fields
    username = entry_username.get()
    password = entry_password.get()

    #checking if username and password match 
    if username == "user" and password == "pass":
        results = "Login successful!"
    else:
        results = "Invalid username or password."

    tk.messagebox.showinfo("Result", results, parent=root)


root = tk.Tk()
root.title("Login Page")
root.geometry("200x200")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
#username for label and entry
label_username = ttk.Label(root, text="Username:")
label_username.grid(row=0, column=0, padx=6, pady=6, sticky="w")

entry_username = ttk.Entry(root, width=20)
entry_username.grid(row=0, column=1, padx=6, pady=6)
#label for password and entry
label_password = ttk.Label(root, text="Password:")
label_password.grid(row=1, column=0, padx=6, pady=6, sticky="w")

entry_password = ttk.Entry(root, width=20, show="*")
entry_password.grid(row=1, column=1, padx=6, pady=6)

#login button
button_login = ttk.Button(root, text="Login", command=on_login)
button_login.grid(row=5, column=0, columnspan=2, padx=6, pady=6)#button place in grid

root.mainloop()