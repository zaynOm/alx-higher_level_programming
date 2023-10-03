#!/usr/bin/python3
"Module for print_square function"


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): The width/height of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less then 0.
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    print('\n'.join(['#' * size] * size))
