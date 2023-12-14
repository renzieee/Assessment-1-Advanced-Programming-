import tkinter as tk

#creating the main window
root = tk.Tk()
root.geometry("300x200")#window size

#creating left frame
frame_left = tk.Frame(root, borderwidth=5) #a frame with border width
frame_left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH) 

#right frame
frame_right = tk.Frame(root, borderwidth=5)  #creating a frame with border width
frame_right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH) #right frame to the right side

# labels A, B, C, and D with border and background color
A_label= tk.Label(frame_left, text="A", border=30, bg="#22263d", fg="white")  
B_label = tk.Label(frame_left, text="B", border=30)  
C_label = tk.Label(frame_right, text="C", border=30)  
D_label = tk.Label(frame_right, text="D", border=30, bg="#22263d", fg="white")  

#labels A, B, C, and D inside their respective frames
A_label.pack(side=tk.TOP, expand=True, fill=tk.X)  
B_label.pack(side=tk.BOTTOM, expand=True, fill=tk.X)  
C_label.pack(side=tk.TOP, expand=True, fill=tk.X)  
D_label.pack(side=tk.BOTTOM, expand=True, fill=tk.X)  

root.mainloop()