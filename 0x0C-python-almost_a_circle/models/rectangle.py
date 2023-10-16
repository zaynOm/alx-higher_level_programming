#!/usr/bin/python3
"Module for Rectangle class"
from .base import Base


class Rectangle(Base):
    "Rectangle shape class."

    def __init__(self, width, height, x=0, y=0, id=None):
        """Inisialize a new Rectangle instanse.

        Args:
            width (int): width of the rectangle.
            height (int): height of the rectangle.
            x (int): Horizontal coordinate.
            y (int): Vertical coordinate.
            id (int): Instance identifier number.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        "int: width getter & setter"
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        "int: height getter & setter"
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        "int: x getter & setter"
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        "int: y getter & setter"
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Area value of the Rectangle instance.

        Returns:
            int: The area of the Rectangle instance.
        """
        return self.width * self.height

    def display(self):
        "prints in stdout the Rectangle instance with the character #."
        print(end='\n' * self.y)
        print('\n'.join([' ' * self.x + '#' * self.width] * self.height))

    def __str__(self):
        "String representation of the instance."
        return (f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - '
                f'{self.width}/{self.height}')

    def update(self, *args, **kwargs):
        """Update the instance attributes.

        Args:
            args (tuple): Tuple of arguments (no-keyword argument)
            kwargs (dict): Dict of arguments (key-worded argument)
        """
        keys = ['id', 'width', 'height', 'x', 'y']
        for i in range(min(len(args), 5)):
            exec(f'self.{keys[i]} = {args[i]}')

        if len(args) == 0:
            for k, v in kwargs.items():
                exec(f'self.{k} = {v}')
