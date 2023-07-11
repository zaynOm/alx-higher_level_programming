#!/usr/bin/python3
"""Defines a function to read a file and print it to stdout"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename (str): Name of the file to read from
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read().rstrip())
