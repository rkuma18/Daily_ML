'''
Write a Python function to calculate the dot product of two vectors. The function should take two 1D NumPy arrays as input and return the dot product as a single number.
'''

import numpy as np

def calculate_dot_product(vec1, vec2):
      '''
        Calculate the dot product of two vectors.
        
	    Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
      '''
      result = np.dot(vec1,vec2)
      return result

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

print(calculate_dot_product(vec1,vec2))