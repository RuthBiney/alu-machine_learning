#!/usr/bin/env python3

"add_matrices2D = __import__('5-across_the_planes').add_matrices2D"


def add_matrices2D(mat1, mat2):
    """Check if matrices have the same shape"""
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    """Create a new matrix to store the result"""
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]

    """ Add corresponding elements element-wise"""
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result
