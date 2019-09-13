import numpy


first_matrix = numpy.arange(3, 12)
first_matrix = first_matrix.reshape(3, 3)

print("Min is", first_matrix.min())
print("Max is", first_matrix.max())
print("Mean is", first_matrix.mean())

second_matrix = first_matrix ** 2

third_matrix = numpy.vstack([first_matrix, second_matrix])

print(numpy.dot(third_matrix, first_matrix))

third_matrix = third_matrix.reshape(3, 3, 2)
print(third_matrix)