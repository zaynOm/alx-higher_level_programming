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

    @staticmethod
    def from_json_string(json_string):
        """JSON string to dictionary.

        Args:
            json_string (str): string representing a list of dictionaries.

        Returns:
            list: list of the JSON string representation json_string.
        """
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set.

        Args:
            dictionary (dict): Dict of arguments (key-worded argument).

        Returns:
            obj: The newly created  Rectangle/Square instance .
        """
        new = cls(1) if cls.__name__ == 'Square' else cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Loads JSON from file than creats new instances.

        Returns:
            list: List of instances if the file exists, otherwise empty list.
        """
        try:
            with open(cls.__name__ + '.json', 'r', encoding='utf-8') as f:
                list_dict = cls.from_json_string(f.read())
                return [cls.create(**d) for d in list_dict]
        except FileNotFoundError:
            return []
