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

    def to_json(self, attrs=None):
        """Returns the dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for item in attrs:
            if hasattr(self, item):
                my_dict[item] = getattr(self, item)
        return my_dict

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance"""
        for k, v in json.items():
            setattr(self, k, v)
