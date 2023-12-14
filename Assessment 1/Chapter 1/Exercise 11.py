#defining the tuple
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009)

#value at index -3
value_at_index_minus_three = year[-3]
print("The value at index -3:", value_at_index_minus_three)

#reversing the tuple and printing the original and reversed tuple
reversed_year = tuple(reversed(year))
print("Original tuple:", year)
print("Reversed tuple:", reversed_year)

#counting the number of times 2009 is at the tuple
count_2009 = year.count(2009)
print("Number of times 2009 appeared:", count_2009)

#getting the index value of 2018
index_2018 = year.index(2018)
print("Index of 2018:", index_2018)

#finding the length of the tuple
tuple_length = len(year)
print("Length of the tuple:", tuple_length)