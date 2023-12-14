#prompting user to input name and age
name = input("Hello user!\nWhat is your name: ").title()
age = int(input("What is your age: "))

#will be calculating the length your name name
length_name= len(name)

#will be calculating the age after one year
year_age= age + 1

#printing the users name
print(f"It is good to meet you, {name}")

#printing the how long your name is 
print(f"The length of your name is:\n{length_name}")

#printing your age after one year
print(f"You will be {year_age} in a year.")