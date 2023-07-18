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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save to file csv"""
        filename = cls.__name__ + ".csv"
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(i.to_dictionary())
        list = cls.to_json_string(list)
        with open(filename, "w") as f:
            f.write(list)

    @classmethod
    def load_from_file_csv(cls):
        """load from file csv"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r") as f:
                list = cls.from_json_string(f.read())
            for i, j in enumerate(list):
                list[i] = cls.create(**list[i])
            return list
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squ
