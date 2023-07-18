#!/usr/bin/python3
"Defines a Square class that inherits from Rectangle"
from .rectangle import Rectangle


class Square(Rectangle):
    """Square shape

    Attributes:
        size (int): Square's sides lenght
        x (int): Vertical coordinates
        y (int): Horizontal coordinates
    """

    def __init__(self, size, x=0, y=0, id=None):
        "Initialize a new Square instance"
        super().__init__(size, size, x, y, id)

    def __str__(self):
        "Override the __str__ so it returns info about the Square"
        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        "Get size"
        return self.width

    @size.setter
    def size(self, size):
        "Set size"
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Update the instance attributes

        Args:
            args (tuple): Tuple of arguments (no-keyword argument)
            kwargs (dict): Dict of arguments (key-worded argument)
        """
        keys = ['id', 'size', 'x', 'y']
        for i in range(len(args)):
            exec(f'self.{keys[i]} = {args[i]}')

        if len(args) == 0:
            for k, v in kwargs.items():
                exec(f'self.{k} = {v}')

    def to_dictionary(self):
        "Returns the dictionary representation of a Square"
        return {'id': self.id, 'x': self.x, 'size': self.width, 'y': self.y}
