#a count variable to keep track of loop iterations
count = 0

#this is an infinite loop
while True:  

    #getting the user input 
    user_input = input("Would you like to continue? (Y/N): ").upper() 

    #if the user enters Y
    if user_input == 'Y': 

        #computing the count if the user enters Y
        count += 1

    #when the users enter N
    elif user_input == 'N':  
        break  
    else:  
        #the user will enter Y or N
        print("It's invalid. Please enter 'Y' or 'N'.")
        continue  #it will continue the loop to get a valid input

#if the loop breaks and if the user entered 'N', it will print the count of loop executions
print(f"The loop was executed {count} times.")