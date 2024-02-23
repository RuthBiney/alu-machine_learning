#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculates the determinant of a matrix, with specific handling for an empty matrix.

    Args:
        matrix (list of lists): The matrix whose determinant is to be calculated.

    Returns:
        int: The determinant of the matrix, with 1 for an empty matrix.

    Raises:
        TypeError: If the matrix is not a list of lists.
        ValueError: If the matrix is not square and not empty.
    """
    # Handling an empty matrix as a special case with a determinant of 1
    if matrix == []:
        return 1

    # Check if the input is a list of lists
    if not all(isinstance(row, list) for row in matrix) or not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")

    # Check if the matrix is square
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix
    if num_rows == 1:
        return matrix[0][0]

    # Recursive case: Calculate determinant for matrices larger than 1x1
    det = 0
    for col in range(num_rows):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        det += (-1) ** col * matrix[0][col] * determinant(minor)

    return det
