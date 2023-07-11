#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """Integer but with (== and !=) operations reversed"""
    def __eq__(num1, num2):
        """Override == with !="""
        return num1 != num2

    def __ne__(num1, num2):
        """Override != with =="""
        return num1 == num2
