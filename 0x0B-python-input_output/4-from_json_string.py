#!/usr/bin/python3
"Module for from_json_string funcion"
import json


def from_json_string(my_str):
    """object from JSON string.

    Args:
        my_str (str): Json representation.

    Returns:
        object: an object (Python data structure) represented by a JSON string.

    """
    return json.loads(my_str)
