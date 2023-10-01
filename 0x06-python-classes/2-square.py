#!/usr/bin/python3
"""a square class definetion"""


class Square:
    """this class defines a square shape.

    Attributes:
        size (int): square sides length.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance

        Args:
            size (int): square sides length, Default to 0

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
