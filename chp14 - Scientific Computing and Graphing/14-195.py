from numpy import arange, vstack, dot

first_matrix = arange(3,12)

first_matrix = first_matrix.reshape(3,3)
print(first_matrix.min())
print(first_matrix.max())
print(first_matrix.mean())

second_matrix = first_matrix ** 2
third_matrix = vstack([first_matrix, second_matrix])

print(dot(third_matrix, first_matrix))
third_matrix = third_matrix.reshape(3, 3, 2)
print(third_matrix)
