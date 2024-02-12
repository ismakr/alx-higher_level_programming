#!/usr/bin/python3
"""rectangle class mod"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get_width"""
        return self.width

    @size.setter
    def size(self, value):
        """set_width"""
        self.width = value
        self.height = value

    def __str__(self):
        """return str"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
