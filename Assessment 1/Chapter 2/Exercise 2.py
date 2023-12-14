from tkinter import *

root = Tk()  #the main window

#creating labels with specified text, width, background color, relief, and border width
ab = Label(root, text="A", width=12, bg="red", relief=GROOVE, bd=5)
bb = Label(root, text="B", width=12, bg="yellow")
bc = Label(root, text="C", width=12, bg="blue")
ba = Label(root, text="D", width=12, bg="white")

#the labels into the main window with specified configurations
ab.pack(side="top", fill=X, expand=1)# placing label A at the top, horizontally stretch to fill the X-axis
bb.pack(side="bottom") #placing a label B at the bottom
bc.pack(side="left", expand=1) #placing label C at the left, horizontally stretch to expand
ba.pack(side="right") #placing label D at the right

root.mainloop()  #starting the GUI
