'''
Write a Python function that multiplies a matrix by a scalar and returns the result.
'''

def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	return [[element * scalar for element in row]for row in matrix]



matrix = [[1, 2], [3, 4]]
scalar = 2

print(scalar_multiply(matrix,scalar))