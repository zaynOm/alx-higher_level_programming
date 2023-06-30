#!/usr/bin/python3
"""a square class definetion"""


class Square:
    """this class defines a square shape.

    Attributes:
        size (int): square sides length.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance

        Args:
            size (int): square sides length, Default to 0
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get size"""
        return self.__size

    @size.setter
    def size(self, size):
        """Set size

        Args:
            size (int): square sides length

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is negative
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def position(self):
        """Get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position

        Args:
            value (int, int): tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate square area

        Returns:
            int: the current square area
        """
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print()
        for _ in range(self.size):
            print(' ' * self.position[0] + '#' * self.size)
