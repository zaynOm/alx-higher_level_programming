#!/usr/bin/python3
"""Defines a function that checks if an object
has the same type as a given class"""


def is_same_class(obj, a_class):
    """checks whether 'obj' is exactly an instance of 'a_class'

    Args:
        obj (object): an instance of a class.
        a_class (class): the class to compare with 'obj'.

    Returns:
        bool: True if 'obj' is an instance of 'a_class'; otherwise False.
    """
    return type(obj) == a_class
