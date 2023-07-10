#!/usr/bin/python3
"""This module contains the 'lookup' function that returns some info
   about a given object.
"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    Args:
        obj (object): a class instance.

    Returns:
        list: all the attributes and methods of 'obj'.
    """

    return dir(obj)
