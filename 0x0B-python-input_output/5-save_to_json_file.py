#!/usr/bin/python3
"""Defines a function that saves an object to a file as json string"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
