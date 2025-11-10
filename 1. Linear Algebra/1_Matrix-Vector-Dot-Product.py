'''
Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.
'''

def matrix_dot_vector(matrix, vector):
    # Check if matrix is empty or vector is empty
    if not matrix or not vector:
        return -1

    # Check matrix consistency (all rows same length)
    num_cols = len(matrix[0])
    if any(len(row) != num_cols for row in matrix):
        return -1  # invalid matrix

    # Check dimension compatibility
    if num_cols != len(vector):
        return -1

    # Compute dot product
    result = []
    for row in matrix:
        dot = sum(row[i] * vector[i] for i in range(num_cols))
        result.append(dot)

    return result


a = [
    [1, 2],
    [2, 4]
]
b = [1, 2]

print(matrix_dot_vector(a, b))   

b2 = [1, 2, 3]
print(matrix_dot_vector(a, b2)) 
