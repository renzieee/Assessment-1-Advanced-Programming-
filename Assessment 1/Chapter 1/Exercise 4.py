#inputing three integers number 
first=int(input("Enter First Number: "))
second=int(input("Enter Second Number: "))
third=int(input("Enter Third Number: "))

#the conditions to find the largest number
if first>second:
    if a>third:
        l=first
    else:
        l=third
else:
    if second>third:
        l=second
    else:
        l=third

#it will print the largest number
print("The Larger number is =",l)