#!/usr/bin/python3
"Module for to_json_string function"
import json


def to_json_string(my_obj):
    """JSON representation of an object.

    Args:
        my_obj: object to serialize.

    Returns:
        str: The json representation of the object.
    """
    return json.dumps(my_obj)
