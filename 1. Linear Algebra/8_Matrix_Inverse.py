'''
Write a Python function that calculates the inverse of a 2x2 matrix. Return 'None' if the matrix is not invertible.
'''
import numpy as np

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    A = np.array(matrix, dtype=float)
    result = np.linalg.inv(A)
    return result.tolist()


matrix = [[4, 7], [2, 6]]
print(inverse_2x2(matrix))

