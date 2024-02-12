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

    def update(self, *args, **kwargs):
        """update the square"""
        if args:
            i = 0
            for ar in args:
                if i == 0:
                    self.id = ar
                elif i == 1:
                    self.size = ar
                elif i == 2:
                    self.x = ar
                elif i == 3:
                    self.y = ar
                i += 1
        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
