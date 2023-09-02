#!/usr/bin/python3
""""up"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix, a list of lists of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with all elements divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If the input matrix is not a list of lists of integers/floats,
                   if the rows of the matrix are not of the same size, or
                   if div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Example:
        >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
        [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    """

    # Check if matrix is a list of lists of integers/floats
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform the matrix division and round to 2 decimal places
    result = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result

# Test cases
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
