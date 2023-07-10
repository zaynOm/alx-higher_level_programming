#!/usr/bin/python3
"""This module provides a function to check if an object
inherits (directly or indirectly) from a specified class"""


def inherits_from(obj, a_class):
    """Check if an object inherits (directly or indirectly)
        from the specified class.

    Args:
        obj: The object to be checked.
        a_class: The class to check against.

    Returns:
        bool: True if the object inherits (directly or indirectly)
              from the specified class, False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
