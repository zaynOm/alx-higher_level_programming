#!/usr/bin/python3
"""A subclass of the list class with a function that prints a sorted list"""


class MyList(list):
    """A subclass of the list class"""
    def print_sorted(self):
        """Prints a list, but sorted (ascending sort)"""
        print(sorted(self))
