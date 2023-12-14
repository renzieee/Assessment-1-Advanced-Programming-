#creating an int list with 10 values
int_list = [17, 29, 43, 56, 81, 92, 14, 67, 12, 23]

#the output using for loop 
print("List:")
for num in int_list:
    print(num, end=" ")  #printing the elements
print() 

#output for the highest and lowest value
high = max(int_list)#finding the highest value
low = min(int_list)#finding the lowest value
print(f"Highest value: {high}")
print(f"Lowest value: {low}")

#elements in ascending order
ascending_order = sorted(int_list)#the list in ascending orders
print("Sort in ascending order:", ascending_order)

#elements in descending order
descending_order = sorted(int_list, reverse=True)#the list in descending order
print("Sort in descending order:", descending_order)

#appending two elements
int_list.append(111)#appending value 111 to the list
int_list.append(5)#appending the value 5 to the list
print("The list after appending two elements:", int_list)