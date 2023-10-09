#!/usr/bin/python3
"Module for BaseGeometry class"


class BaseGeometry:
    "Simple BaseGeometry class"

    def area(self):
        "raises an exception"
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates `value`

        Args:
            name (str): Variable name to validate.
            value (int): Value to validate.

        Raises:
            TypeError: If `value` is not an int.
            ValueError: If `value` is less the or equal to 0.
        """
        if type(value) != int:
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
