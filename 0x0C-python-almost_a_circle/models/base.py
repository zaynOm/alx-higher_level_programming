#!/usr/bin/python3
"Defines a Base class"


class Base:
    "Manages id attribute in all your future classes"
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance.
        Args:
            id (int): New instance's id
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
