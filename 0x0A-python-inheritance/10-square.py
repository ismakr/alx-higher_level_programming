#!/usr/bin/python3
"""square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits from Rectangle"""

    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)
