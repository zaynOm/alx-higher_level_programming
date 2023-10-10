#!/usr/bin/python3
"Module for class_to_json function"


def class_to_json(obj):
    """Class to JSON.

    Args:
        obj: instance of a class.

    Returns:
        dict: the dictionary description for JSON serialization of an object.
    """
    return obj.__dict__
