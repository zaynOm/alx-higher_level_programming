#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = [e for e in my_list]
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    return new_list
