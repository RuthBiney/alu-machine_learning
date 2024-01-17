#!/usr/bin/env python3

"matrix_transpose = __import__('3-flip_me_over').matrix_transpose"
def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix."""
    # Transpose the matrix using list comprehension
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return result