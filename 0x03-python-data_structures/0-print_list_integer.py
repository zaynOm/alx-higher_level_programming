#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list:
        print(*('{:d}'.format(x) for x in my_list), sep='\n')
