'''
multiply two matrices together (return -1 if shapes of matrix don't align)
'''

def matrixmul(a: list[list[int | float]],
              b: list[list[int | float]]) -> list[list[int | float]]:

    # Number of rows and columns
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])

    # Check if multiplication is possible
    if cols_a != rows_b:
        return -1

    # Prepare result matrix with zeros
    result = [[0] * cols_b for _ in range(rows_a)]

    # Multiply
    for i in range(rows_a):           # row of A
        for j in range(cols_b):       # column of B
            for k in range(cols_a):   # common dimension
                result[i][j] += a[i][k] * b[k][j]

    return result


# Test
A = [[1, 2],
     [2, 4]]

B = [[2, 1],
     [3, 4]]

print(matrixmul(A, B))
