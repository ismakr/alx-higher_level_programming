#!/usr/bin/python3
"""base class mod"""


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id not None:
            self.id = id
        else:
            __nb_objects += 1
            self.id = __nb_objects
