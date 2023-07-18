#!/usr/bin/python3
"Defines a Base class"
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        "Returns the JSON string representation of list_dictionaries"
        if list_dictionaries and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        "Writes the JSON string representation of list_objs to a file"
        with open(cls.__name__ + '.json', 'w') as f:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
            f.write(Base.to_json_string(list_dicts))
