'''
Write a Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.
'''
import numpy as np

def calculate_eigenvalues(matrix: list[list[float | int]]) -> list[float]:
    A = np.array(matrix)                     # convert input to numpy array
    eigenvalues = np.linalg.eigvals(A)
    return eigenvalues.tolist()


matrix = [[2, 1], [1, 2]]
print("Eigenvalues:", calculate_eigenvalues(matrix))
