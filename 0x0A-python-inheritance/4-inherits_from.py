#!/usr/bin/python3
"Module for inherits_from function"


def inherits_from(obj, a_class):
    """Checks if object is an instance of a class that inherited
        (directly or indirectly) from the specified class

    Args:
        obj (object): object to check.
        a_class (): class to check against.

    Returns:
        bool: True if obj is an inherited instance of a_class;
        otherwise False.
    """
    return type(obj) != a_class and isinstance(obj, a_class)
