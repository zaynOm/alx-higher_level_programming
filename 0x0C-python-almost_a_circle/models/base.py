#!/usr/bin/python3
"Module for Base class"


class Base:
    "Base class to manage id attribute."

    __nb_objects = 0
    "int: Number of created instances."

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): Instance identifier number.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
