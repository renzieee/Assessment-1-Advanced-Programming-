import tkinter as tk
from tkinter import ttk, PhotoImage

#the main window
root = tk.Tk()
root.title("Student Management System")
root.geometry("550x900")

#creating custom style for frame
style = ttk.Style()
style.configure("TFrame", background="#f4f4f6")

imagelogo = PhotoImage(file="logo.png")
label_images = ttk.Label(root, image=imagelogo)
label_images.pack(pady=(20, 0))

#the header labels
header_labels1 = ttk.Label(root, text="Student Management System", font=("Helvetica", 20, "bold"))
header_labels1.pack(pady=(20, 11))

header_labels2 = ttk.Label(root, text="New Student Registration", font=("Helvetica", 16, "bold"))
header_labels2.pack(pady=(0, 20))
#creating a frame
frame = ttk.Frame(root, padding="50", style="TFrame")
frame.pack()

#entry widgets for the data inputs
entry_name = ttk.Entry(frame)
entry_name.grid(row=0, column=1, padx=11, pady=12)

entry_mobile = ttk.Entry(frame)
entry_mobile.grid(row=1, column=1, padx=12, pady=12)

entry_email = ttk.Entry(frame)
entry_email.grid(row=2, column=1, padx=11, pady=12)

entry_home_address = ttk.Entry(frame)
entry_home_address.grid(row=3, column=1, padx=11, pady=12)

gender_var = tk.StringVar()
combox_gender = ttk.Combobox(frame, textvariable=gender_var)
combox_gender.grid(row=4, column=1, padx=11, pady=12)
combox_gender['values'] = ('Male', 'Female', 'Other')

course_var = tk.StringVar()
combox_course = ttk.Combobox(frame, textvariable=course_var)
combox_course.grid(row=5, column=1, padx=11, pady=12)
combox_course['values'] = ('BSc CC', 'BSc CY', 'BSc PSY', 'BA & BM')

language_var = tk.StringVar()
combox_language = ttk.Combobox(frame, textvariable=language_var)
combox_language.grid(row=6, column=1, padx=11, pady=12)
combox_language['values'] = ('English', 'Tagalog', 'Hindi / Urdu')

#label widgets for data inputs
label_name = ttk.Label(frame, text="Student Name")
label_name.grid(row=0, column=0, padx=11, pady=12)

label_mobile = ttk.Label(frame, text="Mobile Number")
label_mobile.grid(row=1, column=0, padx=11, pady=12)

label_email = ttk.Label(frame, text="Email Id")
label_email.grid(row=2, column=0, padx=11, pady=12)

label_home_address = ttk.Label(frame, text="Home Address")
label_home_address.grid(row=3, column=0, padx=11, pady=12)

label_gender = ttk.Label(frame, text="Gender")
label_gender.grid(row=4, column=0, padx=11, pady=12)

label_course = ttk.Label(frame, text="Course Enrolled")
label_course.grid(row=5, column=0, padx=11, pady=12)

label_language = ttk.Label(frame, text="Language Known")
label_language.grid(row=6, column=0, padx=11, pady=12)

#labels for the english communication skills
english_rating_label = ttk.Label(frame, text="Rate your English communication skills")
english_rating_label.grid(row=7, column=0, padx=11, pady=12)

#slider for the english communications skills
english_rating = ttk.Scale(frame, from_=0, to=11, orient=tk.HORIZONTAL, length=145)
english_rating.grid(row=7, column=1, padx=11, pady=12)


#button
style = ttk.Style()
style.configure("TButton", background="#22263d")

add_button = ttk.Button(frame, text="Submit", style="TButton")
add_button.grid(row=8, column=0, padx=22, pady=5)
clear_button = ttk.Button(frame, text="Clear", style="TButton")
clear_button.grid(row=8, column=1, padx=22, pady=55)

root.mainloop()