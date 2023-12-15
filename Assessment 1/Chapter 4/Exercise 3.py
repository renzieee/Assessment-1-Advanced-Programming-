#reading nums from the file and creating a list of a num
with open('numbers.txt', 'r') as file:
    numbers = [int(line.strip()) for line in file]

#outputing the values
print("List of integers:")
for num in numbers:
    print(num)