#!/usr/bin/python3
"Module for Square class"
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    "Square class that inherits from rectangle"
    def __init__(self, size):
        """Iitialize a new Square instance.

        Args:
            size (int): square side lenght.
        """
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size
