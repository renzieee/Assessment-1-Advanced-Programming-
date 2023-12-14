import json

#asking the user to enter their student details
name = input("Enter student name: ")
number_id = input("Enter student ID: ")
course = input("Enter student course: ")

#creating a dictionary with student details
details_student = {
    "Name": name,
    "ID": number_id,
    "course": course
}

#writing the student details to a JSON file
with open('StudentJson.json', 'w') as file:
    json.dump(details_student, file, indent=4)

#reading the contents from JSON
with open('StudentJson.json', 'r') as file:
    data_student = json.load(file)

#displaying the individual values 
print("Details of the Student are")
print("\tName:", data_student['Name'])
print("\tID:", data_student['ID'])
print("\tcourse:", data_student['course'])

#updated coursedetails for student 1
details_course = {
    "Group": "A",
    "Year": 2
}

#updated students details dictionary with coursedetails
data_student["CourseDetails"] = details_course

#writing the updated data back to the JSON file
with open('StudentJson.json', 'w') as file:
    json.dump(data_student, file, indent=4)

#displaying individual values
print("\nDetails of the Student are")
print("\tName:", data_student['Name'])
print("\tID:", data_student['ID'])
print("\tcourse:", data_student['course'])
print("\tGroup:", data_student['CourseDetails']['Group'])
print("\tYear:", data_student['CourseDetails']['Year'])
