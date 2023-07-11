#!/usr/bin/python3
"""Defines MyInt class"""


class MyInt(int):
    """Integer but with (== and !=) operations reversed"""
    def __eq__(self, num2):
        """Override == with !="""
        return self.real != num2

    def __ne__(self, num2):
        """Override != with =="""
        return self.real == num2
