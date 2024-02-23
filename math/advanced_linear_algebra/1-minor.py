#!/usr/bin/env python3
"""Calculates the minor matrix of a square matrix.
"""


def minor(matrix):
    """
    Calculates the minor matrix of a square matrix.

    Args:
        - matrix (list of lists): The matrix whose minor matrix should be calculated.

    Returns:
        - list of lists: The minor matrix of the input matrix.

    Raises:
        - TypeError: If matrix is not a list of lists.
        - ValueError: If matrix is not square or is empty.

    Note:
        - The list [[]] represents a 0x0 matrix.
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if the matrix is square and non-empty
    num_rows = len(matrix)
    if num_rows == 0 or num_rows != len(matrix[0]):
        raise ValueError("matrix must be a non-empty square matrix")

    # Calculate the minor matrix
    minor_mat = []
    for i in range(num_rows):
        minor_row = []
        for j in range(num_rows):
            # Calculate the minor of the (i, j) element
            minor_value = determinant([row[:j] + row[j + 1:]
                                      for row in (matrix[:i] + matrix[i + 1:])])
            minor_row.append(minor_value)
        minor_mat.append(minor_row)

    return minor_mat
