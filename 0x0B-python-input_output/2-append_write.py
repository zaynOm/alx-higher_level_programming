#!/usr/bin/python3
"Module for append_write function"


def append_write(filename="", text=""):
    """appends a string to the end of a text file.

    Args:
        filename (str): The file name to append to.
        text (str): The content to append.

    Returns:
        int: number to written characters.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
