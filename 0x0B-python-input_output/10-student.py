#!/usr/bin/python3
"Module for Student class"


class Student:
    "Student class"
    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance.

        Args:
            first_name (str): Students first name.
            last_name (str): Students last name.
            age (int): Students age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance.

        Args:
            attrs (list/None): contains attribute names to retrieve.

        Returns:
            dict: attributes contained in `attrs`; or all attributes.
        """
        if attrs:
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
