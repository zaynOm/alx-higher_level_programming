#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates 'value' parameter

        Args:
            name (str): parameters name
            value (int): parameter to validate

        Raises:
            TypeError: If 'value' is not an integer
            ValueError: If 'value' is less or equal to 0
        """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
