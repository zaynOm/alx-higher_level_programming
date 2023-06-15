#!/usr/bin/python3
def roman_to_int(roman_string):
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev_value = 0
    for c in reversed(roman_string):
        value = nums.get(c, 0)
        if value < prev_value:
            res -= value
        else:
            res += value
            prev_value = value
    return res
