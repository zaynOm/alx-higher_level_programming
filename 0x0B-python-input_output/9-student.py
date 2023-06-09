#!/usr/bin/python3
"""Defines a Student class"""


class Student:
    """Student class inplementation."""
    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance

        Args:
            first_name (str): Students first name.
            last_name (str): Students last name.
            age (int): Students age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Returns the dictionary representation of a Student"""
        return self.__dict__
