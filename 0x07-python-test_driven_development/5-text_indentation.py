#!/usr/bin/python3
"Module for text_indentation function."


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): string to print.

    Raises:
        TypeError: if `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for delim in '.:?':
        text = (delim + '\n\n').join(ln.strip() for ln in text.split(delim))

    print(text, end='')
