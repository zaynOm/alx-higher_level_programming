#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from 'BaseGeometry' class

    Attributes:
        width (int): width of the Rectangle
        height (int): height of the Rectangle
    """
    def __init__(self, width, height):
        """Initializes width and height after validation

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Return rectangle info in a string format"""
        return f"[Rectangle] {self.__width}/{self.__height}"
