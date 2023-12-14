import matplotlib.pyplot as plt

#for the first line from (1, 2) to (6, 8)
x1_values = [1, 6]
y1_values = [2, 8]

#for the dotted line from (1, 3) to (2, 8) to (6, 1) to (8, 10)
values_x2 = [1, 2, 6, 8]
values_y2 = [3, 8, 1, 10]

#creating a new figure
plt.figure(figsize=(8, 6))

#plot of the first line (solid)
plt.plot(x1_values, y1_values, label='Line 1')

#plot of the dotted line
plt.plot(values_x2, values_y2, linestyle=':', marker='o', label='Dotted Line')

#x and y axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#plot title
plt.title('Lines on a Diagram')

#display the legend
plt.legend()

# Display the plot
plt.show()
