#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        print(*('{:d}'.format(e) for e in reversed(my_list)), sep='\n')
