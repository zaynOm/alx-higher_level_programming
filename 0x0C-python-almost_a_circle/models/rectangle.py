#!/usr/bin/python3
"Defines a Rectangle class that inherits from Base"
from .base import Base


class Rectangle(Base):
    """Rectangle shape

    Attributes:
        width (int): Rectangle's width
        height (int): Rectangle's height
        x (int): Vertical coordinates
        y (int): Horizontal coordinates
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        "Override the __str__ so it returns info about the Rectangle"
        return (f'[Rectangle] ({self.id}) {self.x}/{self.y}'
                f' - {self.width}/{self.height}')

    @property
    def width(self):
        "Get width"
        return self.__width

    @width.setter
    def width(self, width):
        "Set width"
        if type(width) != int:
            raise TypeError('width must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        self.__width = width

    @property
    def height(self):
        "Get height"
        return self.__height

    @height.setter
    def height(self, height):
        "Set height"
        if type(height) != int:
            raise TypeError('height must be an integer')
        if height <= 0:
            raise ValueError('height must be > 0')
        self.__height = height

    @property
    def x(self):
        "Get x"
        return self.__x

    @x.setter
    def x(self, x):
        "Set x"
        if type(x) != int:
            raise TypeError('x must be an integer')
        if x < 0:
            raise ValueError('x must be >= 0')
        self.__x = x

    @property
    def y(self):
        "Get y"
        return self.__y

    @y.setter
    def y(self, y):
        "Set y"
        if type(y) != int:
            raise TypeError('y must be an integer')
        if y < 0:
            raise ValueError('y must be >= 0')
        self.__y = y

    def area(self):
        "Returns the area value of the Rectangle instance"
        return self.width * self.height

    def display(self):
        "Prints the rectangle instance with the character '#'"
        print(end='\n' * self.y)
        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def update(self, *args, **kwargs):
        """Update the instance attributes

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

    def to_dictionary(self):
        "Returns the dictionary representation of a Rectangle"
        return {'x': self.x, 'y': self.y, 'id': self.id,
                'height': self.height, 'width': self.width}
