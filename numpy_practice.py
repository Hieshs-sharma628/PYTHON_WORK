import numpy as np

# Example 1D array used for practice operations
a = np.array([12, 45, 67, 23, 89, 34, 56, 78, 91, 15])

# access first element (index 0)
print("1st element:", a[0])

# access last element using negative index
print("Last element:", a[-1])

# access fourth element (index 3)
print("4th element:", a[3])

# slice: last three elements
print("Last 3 elements:", a[-3:])

# slice: first five elements
print("First 5 elements:", a[:5])

# scalar: maximum value in the array
print("Maximum element:", a.max())

# scalar: minimum value in the array
print("Minimum element:", a.min())

# sum of all elements
print("Sum of all elements:", a.sum())

# mean (average) of the elements
print("Mean of all elements:", a.mean())

# boolean indexing: elements greater than 50
print("Elements > 50:", a[a > 50])

# boolean indexing: even elements
print("Even elements:", a[a % 2 == 0])

# boolean indexing: odd elements
print("Odd elements:", a[a % 2 != 0])

# add 10 to each element (vectorized)
print("Add 10 to each element:", a + 10)

# multiply each element by 2 (vectorized)
print("Multiply each element by 2:", a * 2)

# boolean mask: elements less than 40
less = a < 40
print("Elements < 40:", a[less])

# boolean mask: elements greater than 60
greater = a > 60
print("Elements > 60:", a[greater])

# index of the largest element
largest_index = a.argmax()
print("Index of largest element:", largest_index)

# sorted copy of the array
sort_a = np.sort(a)
print("Sorted array:", sort_a)

# reversed (flipped) copy of the array
revers_a = np.flip(a)
print("Reversed array:", revers_a)

# standard deviation of elements
sd = a.std()
print("Standard deviation:", sd)


# Working with a 2D array (matrix)
m = np.array([
	[10, 20, 30],
	[40, 50, 60],
	[70, 80, 90]
])

# access second row (index 1)
print("Second row:", m[1])

# access third column (all rows, column index 2)
print("Third column:", m[:, 2])

# access center element (row 1, column 1)
print("Center element:", m[1, 1])

# shape: (rows, columns)
print("Shape of matrix:", m.shape)

# sum across columns for each row (axis=1)
sum_m = np.sum(m, axis=1)
print("Sum of each row:", sum_m)

# sum across row for each columns (axis=1)
sum_m = np.sum(m, axis=0)
print("Sum of each row:", sum_m)

# element-wise multiply entire matrix by 5
print("Matrix multiplied by 5:", m * 5)

# boolean mask: elements greater than 45
greater_45 = m > 45
print("Elements > 45:", m[greater_45])

# maximum across entire matrix
print("Maximum element in matrix:", m.max())

# flatten matrix to 1D array
flatten_m = m.flatten()
print("Flattened form:", flatten_m)
