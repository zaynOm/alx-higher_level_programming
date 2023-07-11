#!/usr/bin/python3
"""Defines a function that craets an object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creats an Object from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
