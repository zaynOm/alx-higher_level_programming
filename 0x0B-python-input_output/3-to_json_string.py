#!/usr/bin/python3
"""Serializes to JSON string"""
import json


def to_json_string(my_obj):
    """Objects to JSON string

    Args:
        my_obj (obj): Object to serialize

    Returns:
        str: JSON string
    """
    return json.dumps(my_obj)
