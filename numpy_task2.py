import numpy as np

scores = np.array([78, 45, 89, 92, 56, 73, 88, 61, 99, 67])

#Average score
print("Average of scores :: ",scores.mean())

#replace all scores below 60 with 0
scores[scores < 60]=0
print("Replace array:: ",scores)

#top 3 highest scores
largest_three= np.sort(scores)
print("Three highest ",largest_three[-3:])

# Count how many students scored at least 75.
print("Count of student ::",np.count_nonzero(scores >= 75))

# Convert the array into a 2×5 matrix.
reshape=scores.reshape(2,5)
print("Reshaped array ::",reshape)

# Find the average of each row.
print("Average of each row",reshape.mean(axis=1))

# Find the average of each column.
print("Average of each column",reshape.mean(axis=0))

# Check the shape.
print("Shape of array :: ", reshape.shape)

# Print the first row.
print("First row :: ", reshape[0])

# Print the second column.
print("Second column :: ", reshape[:,1])

# Print the last column.
print("last column :: ", reshape[:,-1])

# Find the sum of each row.
print("Sum of rows ", reshape.sum(axis=1))

# Find the sum of each column.
print("Sum of column ", reshape.sum(axis=0))

# Find the average of each row.
print("Average of row ", reshape.mean(axis=1))

# Find the average of each column.
print("Average of column ", reshape.mean(axis=0))

# Find the maximum value in each row.
print("Max value of rows ", reshape.max(axis=1))

# Find the minimum value in each column
print("Max value of column ", reshape.max(axis=0))

#clreating array score with value between
score=np.arange(60,91)
print(score)

#return index of element that is greater than 80
indices=np.where(score > 80)
print(indices)
