#!/usr/bin/python3
"""Defines a function to write to a file"""


def write_file(filename="", text=""):
    """Writes a string to a text file.

    Args:
        filename (str): Files name to write to.
        text (str): Content to write to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
