#!/usr/bin/python3
"Module for add_attribute function"


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj: The object to add an attribute to.
        att (str): The name of the attribute.
        value: The value of attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
