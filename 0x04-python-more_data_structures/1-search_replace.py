#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [e if e != search else replace for e in my_list]
