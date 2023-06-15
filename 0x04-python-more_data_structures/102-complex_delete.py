#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    rem = list(filter(lambda p: p[1] == value, a_dictionary.items()))
    for e in rem:
        del a_dictionary[e[0]]
    return a_dictionary
