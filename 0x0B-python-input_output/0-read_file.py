#!/usr/bin/python3
"Module for read_file function"


def read_file(filename=""):
    """reads a text file and prints it.

    Args:
        filename (str): The file name to read.
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end='')
