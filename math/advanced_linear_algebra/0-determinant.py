#!/usr/bin/env python3
"""
    a function def determinant(matrix):
    that calculates the determinant of a matrix:
"""


def determinant(matrix):
    """
    Calculates the determinant of a matrix.

    

    Raises:
        TypeError: If the matrix is not a list of lists.
        ValueError: If the matrix is not square.

    """
    # Check if the input is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check for an empty matrix
    if len(matrix) == 0:
        return 1  # The determinant of an empty matrix is considered 1

    # Check if the matrix is square
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if num_rows == 1:
        return matrix[0][0]

    # Recursive case: Calculate determinant
    det = 0
    for col in range(num_rows):
        minor = [row[:col] + row[col + 1:]
                 for row in matrix[1:]]  # Get the minor of the current element
        det += (-1) ** col * matrix[0][col] * \
            determinant(minor)  # Recursive call

    return det
