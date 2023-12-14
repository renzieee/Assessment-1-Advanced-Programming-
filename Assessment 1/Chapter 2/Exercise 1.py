import tkinter as tk

root = tk.Tk()
root.geometry("500x400") #default window size
root.resizable(False, False) #disabling the resizing window
root.configure(bg="green") #background color

#function for changing the label font style
def change_font():
    label_welcome.config(font=("Times", 30, "bold"))

#displaying the welcome message
label_welcome = tk.Label(root, text="Welcome!!!", font=("Helvetica", 17,), bg="beige")
label_welcome.pack(pady=50)#adjusting the label's vertical position 

#the button to change the font style
button_font = tk.Button(root, text="Change the Font", command=change_font)
button_font.pack()#the button for window

root.mainloop()