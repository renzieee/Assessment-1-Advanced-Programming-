#entering the first side of the triangle
side1 = int(input("Pleaser enter first side of the triangle : "))

#entering the second side of the triangle
side2= int(input("Please enter second side of the triangle : "))

#entering the third side of the triangle
side3 = int(input("Please enter third side of the triangle : "))

#the conditions whether the triangle can be formed or not
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2 :

    #if its possible it will say that it is a triangle
    print("It is a triangle")

    #if its not possible it will say that it is not a triangle
else :
    print("It is not a triangle")