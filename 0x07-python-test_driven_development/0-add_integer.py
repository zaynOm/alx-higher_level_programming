#!/usr/bin/python3
"""This module has a function that adds 2 integers."""


def add_integer(a, b=98):
    """adds two integers.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of 'a' and 'b'.

    Raises:
        TypeError: If 'a' or 'b' are neither int nor float.
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
