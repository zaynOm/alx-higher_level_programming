#!/usr/bin/python3
"finds a peak in a list of unsorted integers."


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): List of unsorted integers.

    Rerurns:
        int/None: The peak number, None if peak was not found
    """

    if not list_of_integers:
        return None

    l, r = 0, len(list_of_integers) - 1

    while l < r:
        m = (l + r) // 2

        if list_of_integers[m] > list_of_integers[m + 1]:
            r = m
        else:
            l = m + 1
    return list_of_integers[l]
