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

    @staticmethod
    def from_json_string(json_string):
        "returns the list of the JSON string representation json_string"
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        "Writes the JSON string representation of list_objs to a file"
        with open(cls.__name__ + '.json', 'w') as f:
            if list_objs is None:
                f.write('[]')
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        "returns an instance with all attributes already set"
        if cls.__name__ == "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ == "Square":
            dum = cls(1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        "returns a list of instances"
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as f:
                list = cls.from_json_string(f.read())
            for i, j in enumerate(list):
                list[i] = cls.create(**list[i])
            return list
        except FileNotFoundError:
            return []
