#listing the array
a = [20, 23, 82, 40, 32, 15, 67, 52]

#finding indices of even numbers
even_indice = [index for index, num in enumerate(a) if num % 2 == 0]
print("Indices of even numbers:", even_indice)

#sorting the arrays
sort_a = sorted(a)
print("Sorted array:", sort_a)

#slicing elements from index from 3 to the end of array
slicing_end = a[3:] #slicing the index from 3 to the end
print("Elements from index 3 to end:", slicing_end)

#slicing elements from index from 0 to the index 4
slicing_start_end = a[0:5]  #slicing the index from 0 to index 4 (exclusive)
print("Elements from index 0 to index 4:", slicing_start_end)

#printing [32, 15, 67] and using negative slicing
slice_negative = a[-5:-2]  #negative slicing to get the elements from index -5 to -2
print("Using negative slicing to get [32, 15, 67]:", slice_negative)
