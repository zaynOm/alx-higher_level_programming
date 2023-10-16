#!/usr/bin/python3
"Module for Square class."
from models.rectangle import Rectangle


class Square(Rectangle):
    "Square shape class."

    def __init__(self, size, x=0, y=0, id=None):
        """Inisialize a new Square instanse.

        Args:
            size (int): side of the square.
            x (int): Horizontal coordinate.
            y (int): Vertical coordinate.
            id (int): Instance identifier number.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "String representation of a square instance."
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        "int: size getter & setter"
        return self.width

    @size.setter
    def size(self, value):
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Update the instance attributes.

        Args:
            args (tuple): Tuple of arguments (no-keyword argument)
            kwargs (dict): Dict of arguments (key-worded argument)
        """
        keys = ['id', 'size', 'x', 'y']
        for i in range(min(len(args), 4)):
            exec(f'self.{keys[i]} = {args[i]}')

        if len(args) == 0:
            for k, v in kwargs.items():
                exec(f'self.{k} = {v}')
