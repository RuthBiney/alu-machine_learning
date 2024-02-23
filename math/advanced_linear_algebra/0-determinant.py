#!/usr/bin/env python3
def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Parameters:
    - matrix (list of lists): The matrix whose determinant should be calculated.

    Returns:
    - float: The determinant of the matrix.

    Raises:
    - TypeError: If matrix is not a list of lists.
    - ValueError: If matrix is not square.

    Note:
    - The list [[]] represents a 0x0 matrix.
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if the matrix is square
    num_rows = len(matrix)
    if num_rows != len(matrix[0]):
        if num_rows == 0:
            return 1
        else:
            raise ValueError("matrix must be a square matrix")

    # Base case: 1x1 matrix has determinant equal to its only element
    if num_rows == 1:
        return matrix[0][0]

    # Base case: 2x2 matrix determinant calculation
    if num_rows == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    # Recursive case: calculate determinant using Laplace expansion
    det = 0
    for j in range(num_rows):
        sign = (-1) ** j
        sub_matrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        det += sign * matrix[0][j] * determinant(sub_matrix)

    return det
