import tkinter as tk
from tkinter import messagebox

def validate_password():
    attempts_remaining = 5
    #loop to for maximum attempts
    while attempts_remaining > 0:
        password = entry_password.get()

        #password criteria 
        if len(password) < 6 or len(password) > 12:
            messagebox.showwarning("Invalid Password", "Password length should be between 6 and 12 characters.")
        elif not any(charac.islower() for charac in password):
            messagebox.showwarning("Invalid Password", "Password should contain at least 1 lowercase letter (a-z).")
        elif not any(charac.isupper() for charac in password):
            messagebox.showwarning("Invalid Password", "Password should contain at least 1 uppercase letter (A-Z).")
        elif not any(charac.isdigit() for charac in password):
            messagebox.showwarning("Invalid Password", "Password should contain at least 1 digit (0-9).")
        elif not any(charac in "$#@ " for charac in password):
            messagebox.showwarning("Invalid Password", "Password should contain at least one of '$', '#', '@'.")
        else:
            messagebox.showinfo("Valid Password", "Password is valid.")
            break  #brakingg the loop if the password is valid
        
        attempts_remaining -= 1
        #handing the attempts count and alerting 
        if attempts_remaining > 0:
            messagebox.showwarning("Attempts Remaining", f"{attempts_remaining} attempts remaining.")
        else:
            messagebox.showerror("Alert!", "Authorities have been alerted!")
            break  #breaking the loop if attempts reach the limit

#main window
root = tk.Tk()
root.title("Password Validator")
root.geometry("300x300")

#widget for the password input
label_password = tk.Label(root, text="Enter Password:")
label_password.pack(pady=11)

entry_password = tk.Entry(root, show="*") 
entry_password.pack(pady=11)

#button for checking the password validity
validate_button = tk.Button(root, text="Check Password", command=validate_password)
validate_button.pack(pady=21)

root.mainloop()
