#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size):
        """Initializes a new Square

        Args:
            size (int): lenght of the squares side
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
