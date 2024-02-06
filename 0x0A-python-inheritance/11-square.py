#!/usr/bin/python3
"""square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""

    def __init__(self, size):
        """ini the square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """return, the square description"""
        return f"[Square] {self.__size}/{self.__size}"
