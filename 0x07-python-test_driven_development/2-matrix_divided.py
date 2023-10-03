#!/usr/bin/python3
"matrix_divided function"


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): List of lists of integers or floats.
        div (int/float): The divisor.

    Raises:
        TypeError: If matrix is not list of lists of integers or floats.
        TypeError: If the matrix dosen't have the same size.
        TypeError: If div is neither integer nor float.
        ZeroDivisionError: If div is zero.

    Returns:
        A new matrix containing the result of the division.
    """

    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) and
                    all(isinstance(e, (int, float)) for e in row)
                    for row in matrix)):
        raise TypeError('matrix must be a matrix (list of lists) '
                        'of integers/floats')

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    if type(div) != int and type(div) != float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    return [[round(e / div, 2) for e in row] for row in matrix]
