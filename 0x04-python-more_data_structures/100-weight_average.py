#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    res, weight = 0, 0
    for n1, n2 in my_list:
        res += n1 * n2
        weight += n2
    return res / weight
