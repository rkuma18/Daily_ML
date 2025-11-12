'''
Task: Implement Cosine Similarity
In this task, you need to implement a function cosine_similarity(v1, v2) that calculates the cosine similarity between two vectors. Cosine similarity measures the cosine of the angle between two vectors, indicating their directional similarity.

Input:
v1 and v2: Numpy arrays representing the input vectors.
Output:
A float representing the cosine similarity, rounded to three decimal places.
Constraints:
Both input vectors must have the same shape.
Input vectors cannot be empty or have zero magnitude.
'''

import numpy as np

def cosine_similarity(v1, v2):
    # --- Validation Checks ---
    if v1.shape != v2.shape:
        raise ValueError("Both vectors must have the same shape.")
    if v1.size == 0 or v2.size == 0:
        raise ValueError("Input vectors cannot be empty.")
    
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    
    if norm_v1 == 0 or norm_v2 == 0:
        raise ValueError("Input vectors cannot have zero magnitude.")
    
    # --- Cosine Similarity Formula ---
    dot_product = np.dot(v1, v2)
    cosine_sim = dot_product / (norm_v1 * norm_v2)
    
    # --- Return rounded value ---
    return round(float(cosine_sim), 3)


# Example Test
v1 = np.array([1, 2, 3])
v2 = np.array([2, 4, 6])

print(cosine_similarity(v1, v2)) 

