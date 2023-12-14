#it will get two integer numbers from the user
num1 = int(input("Enter the first integer number: "))
num2 = int(input("Enter the second integer number: "))

#it will perform calculations
result_sum = num1 + num2
result_difference = num1 - num2
result_product = num1 * num2

#checking if the second number is not zero for division
if num2 != 0:
    result_division = num1 / num2
else:
    result_division = "Cannot divide by zero"

#calculating remainder only if the second number is not zero
if num2 != 0:
    result_remainder = num1 % num2
else:
    result_remainder = "Cannot calculate remainder, second number is zero"

#output of the results
print(f"Sum: {result_sum}")
print(f"Difference: {result_difference}")
print(f"Product: {result_product}")
print(f"Division: {result_division}")
print(f"Remainder: {result_remainder}")