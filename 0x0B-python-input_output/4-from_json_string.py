#!/usr/bin/python3
"""Deserializes a JSON string"""
import json


def from_json_string(my_str):
    """JSON string to object

    Args:
        my_str (str): JSON string to deserialize

    Returns:
        obj: Python object
    """
    return json.load(my_str)
