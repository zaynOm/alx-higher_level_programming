#!/usr/bin/python3
"Module for MyInt class"


class MyInt(int):
    "MyInt class that inherits from int."
    def __eq__(self, other):
        "invers == operator"
        return self.real != other

    def __ne__(self, other):
        "invers != operator"
        return super().__eq__(other)
