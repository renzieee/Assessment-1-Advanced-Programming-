
for num in range(1, 101):
    #checking if the numbers can be divided by 3 or 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")#it will print fizzbuzz if its divisible by 3 or 5
    #it will check if the numbers can be divided by 3
    elif num % 3 == 0:
        print("Fizz")#it will print fizz if divisible by 3
    #checking if the numbers can be divided by 5
    elif num % 5 == 0:
        print("Buzz") #it will print buzz if the number is divded by 5
    else:
        print(num)#printing the numbers itself