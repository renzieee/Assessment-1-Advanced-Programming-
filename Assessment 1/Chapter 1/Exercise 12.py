import math  #importing math

#a function to calculate the are of the square
def calculate_square_area():
    side = float(input("Enter the side length of the square: "))#asking the user for side length
    area = side ** 2#calculating the are of the square
    print(f"The area of the square is: {area}") #printing the calculated area

#a function to calculate area of the circle
def calculate_circle_area():
    r = float(input("Enter the radius of circle: "))#asking user for radius
    a = math.pi * (r ** 2)  #area of the circle using pi * r^2 formula
    print(f"The area of the circle is: {a}")#printing the calculated area

#the fucntion to calculate the area of a triangle
def calculate_triangle_area():
    b = float(input("Enter the base length of triangle: "))# asking the user for base length
    h = float(input("Enter the height of the triangle: "))  #asking the user for height
    ar = 0.5 * b * h  # calculating area of the triangle using (base * height) / 2 formula
    print(f"The area of the triangle is: {ar}") #printing the calculated area

#displaying the menu and what are the player wants to calculate
while True:
    print("What do you want to Calculate\nMenu:")
    print("1: Calculate the area of a square")
    print("2: Calculate the area of a circle")
    print("3: Calculate the area of a triangle")

    choice = input("Enter your choice (1/2/3): ") #asking the user for their choice

    if choice == '1':
        calculate_square_area() #function to calculate square
    elif choice == '2':
        calculate_circle_area()  #function to calculate circle 
    elif choice == '3':
        calculate_triangle_area()  #function to calculate triangle
    else:
        print("Invalid choice. Please enter a valid option.")  #error message for invalid input
