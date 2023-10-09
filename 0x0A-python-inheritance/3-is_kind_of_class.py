#!/usr/bin/python3
"Moduel for is_kind_of_class function"


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of, or if it's an instance
    of a class that inherited from, the specified class ; otherwise False."""
    return isinstance(obj, a_class)
