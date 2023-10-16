#!/usr/bin/python3
"Module for Base class"
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string.

        Args:
            list_dictionaries (list of dict): List of dictionaries representing
                an instance.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file.

        Args:
            list_objs (list of objects): list of instances who inherits
                of Base.
        """
        l_dict = [e.to_dictionary() for e in list_objs] if list_objs else None
        with open(cls.__name__ + '.json', 'w', encoding='utf-8') as f:
            f.write(cls.to_json_string(l_dict))
