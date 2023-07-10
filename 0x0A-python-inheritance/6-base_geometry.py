#!/usr/bin/python3
"""Defines a BaseGeometry class"""


class BaseGeometry:
    """Base geometry class"""
    def area(self):
        """raises an Exception with the message area() is not implemented"""
        raise Exception("area() is not implemented")
