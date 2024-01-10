#!/usr/bin/python3
"finds a peak in a list of unsorted integers."


def find_peak(list_of_integers):
    if len(nums) == 1:
        return 0
    for idx, e in enumerate(list_of_integers):
        # check the first element in the list
        if idx == 0 and e >= list_of_integers[idx + 1]:
            return e
        # check the last element in the list
        if idx == len(list_of_integers) - 1 and list_of_integers[idx - 1] <= e:
            return e
        # check for element inside the list
        if list_of_integers[idx - 1] <= e and e >= list_of_integers[idx + 1]:
            return e
    return None
