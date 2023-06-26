#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        num = 0
        for e in my_list[:x]:
            print(e, end='')
            num += 1
        print()
        return num
    except IndexError:
        raise IndexError
