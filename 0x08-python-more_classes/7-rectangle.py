#!/usr/bin/python3
"Simple class"


class Rectangle:
    "Defines a rectangle class"

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        "Initialize a new rectangle instance"
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        "returns the rectangle area."
        return self.width * self.height

    def perimeter(self):
        "returns the rectangle perimeter."
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        "Returns the rectangle represented by #"
        if not (self.width or self.height):
            return ''
        return '\n'.join([str(self.print_symbol) * self.width] * self.height)

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return f'Rectangle({self.width}, {self.height})'

    def __del__(self):
        "Runs when an instance of Rectangle is deleted"
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1
