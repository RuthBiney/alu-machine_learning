#!/usr/bin/env python3

"cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D"
def cat_matrices2D(mat1, mat2, axis=0):
    if axis == 0:
        # Check if the matrices have the same number of columns
        if len(mat1[0]) != len(mat2[0]):
            return None

        # Concatenate along the rows (axis=0)
        result = mat1 + mat2

    elif axis == 1:
        # Check if the matrices have the same number of rows
        if len(mat1) != len(mat2):
            return None

        # Concatenate along the columns (axis=1)
        result = [row1 + row2 for row1, row2 in zip(mat1, mat2)]

    else:
        # Invalid axis value
        return None

    return result
