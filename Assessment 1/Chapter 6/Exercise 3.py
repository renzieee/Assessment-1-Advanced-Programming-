import operator

#function of each operation
def add(a, b):
    return operator.add(a, b)

def subtract(a, b):
    return operator.sub(a, b)

def multiply(a, b):
    return operator.mul(a, b)

def divide(a, b):
    return operator.truediv(a, b)

def modulus(a, b):
    return operator.mod(a, b)

def greater_number(a, b):
    return operator.gt(a, b)

#showing the calculator menu
print("Calculator Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Check greater number")

#getting the user's choices of operation
choices = int(input("Enter your choices (1-6): "))

#getting the input values for calculation
value1 = float(input("Enter first value: "))
value2 = float(input("Enter second value: "))

#performing the calculation based on user's choices
if choices == 1:
    results = add(value1, value2)
elif choices == 2:
    results = subtract(value1, value2)
elif choices == 3:
    results = multiply(value1, value2)
elif choices == 4:
    results = divide(value1, value2)
elif choices == 5:
    results = modulus(value1, value2)
elif choices == 6:
    results = greater_number(value1, value2)
    if results:
        print(f"{value1} is greater than {value2}")
    else:
        print(f"{value2} is greater than {value1}")
    exit()
else:
    print("Invalid choices")
    exit()

#results of the calculation
print("results:", results)
