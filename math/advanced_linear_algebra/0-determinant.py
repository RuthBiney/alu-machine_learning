#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculates the determinant of a matrix, with specific handling for an empty matrix
    and validation for square matrices.

    Args:
        matrix (list of lists): The matrix whose determinant is to be calculated.

    Returns:
        int or float: The determinant of the matrix.

    Raises:
        TypeError: If the matrix is not a list of lists.
        ValueError: If the matrix is not square (except for an empty matrix).
    """
    # Special handling for an empty matrix, interpreted as a 0x0 matrix with a determinant of 1
    if matrix == []:
        return 1

    # Validate matrix format and square shape
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")
    num_rows = len(matrix)
    for row in matrix:
        if len(row) != num_rows:
            raise ValueError("matrix must be a square matrix")

    # Handling for a 1x1 matrix
    if num_rows == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    # Calculate determinant for matrices larger than 1x1
    det = 0
    for col in range(num_rows):
        minor = [row[:col] + row[col+1:]
                 for row in matrix[1:]]  # Create minor matrix
        det += (-1) ** col * matrix[0][col] * \
            determinant(minor)  # Recursive call

    return det
