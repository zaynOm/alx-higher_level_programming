#!/usr/bin/python3
"Module for write_file function"


def write_file(filename="", text=""):
    """writes a string to a text file.

    Args:
        filename (str): The file name to write to.
        text (str): The content to write.

    Returns:
        int: number to written characters.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
