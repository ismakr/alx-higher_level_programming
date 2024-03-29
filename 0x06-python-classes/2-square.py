#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square by:
        Private instance attribute: size"""
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")
