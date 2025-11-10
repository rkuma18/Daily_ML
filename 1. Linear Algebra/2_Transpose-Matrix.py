'''
Write a Python function that computes the transpose of a given matrix.
'''

import numpy as np

def transpose(a):
    return np.transpose(a).tolist()  # convert back to list of lists

a = [[1, 2, 3], [4, 5, 6]]
print(transpose(a))
