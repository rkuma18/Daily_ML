'''
Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
'''

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty.")
    
    if mode == 'row':
        # Mean of each row
        mean = [sum(row) / len(row) for row in matrix]
    elif mode == 'column':
        # Transpose to access columns and compute mean
        num_cols = len(matrix[0])
        mean = [sum(matrix[i][j] for i in range(len(matrix))) / len(matrix) for j in range(num_cols)]
    else:
        raise ValueError("Mode must be either 'row' or 'column'.")
    
    return mean


# Example usage
matrix = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]
mode = 'row'

print(calculate_matrix_mean(matrix, mode))
