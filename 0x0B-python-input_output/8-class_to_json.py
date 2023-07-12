#!/usr/bin/python3
"""Defines a function that convert a class info into a dict"""


def class_to_json(obj):
    """returns the dictionary description of a class"""
    return obj.__dict__
