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
        self.__width = value

    @property
    def height(self):
        "int: height getter & setter"
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        "int: x getter & setter"
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        "int: y getter & setter"
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
