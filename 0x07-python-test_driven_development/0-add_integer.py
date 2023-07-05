#!/usr/bin/python3
"""This is "0-add_integer" module that supplies one function add_integer()"""

def add_integer(a, b=98):
    """adds two integers

    Args:
        a (int): first number
        b (int): seccond number

    Returns:
        int: The addition of a and b

    Raises:
        TypeError: If 'a' or 'b' are nether int nor float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)


