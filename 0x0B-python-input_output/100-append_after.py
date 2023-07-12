#!/usr/bin/python3
"""Defines a function that adds text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Adds a line to a file, after each one containing a specific string"""
    with open(filename, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
