#!/usr/bin/python3
"""rectangle class mod"""
from models.base import Base


class Rectangle(Base):
    """class rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get_width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set_width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get_height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set_height"""
        if not isinstance(value, int):
            raise TypeError(f"height must be an integer")
        if value <= 0:
            raise ValueError(f"height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get_x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set_x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get_y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set_y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle"""
        i = 0
        k = 0
        while k < self.__y:
            print("")
            k += 1
        while i < self.height:
            k = 0
            while k < self.__x:
                print(" ", end="")
                k += 1
            j = 0
            while j < self.width:
                print("#", end="")
                j += 1
            print("")
            i += 1

    def __str__(self):
        """return str"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update the rectangle"""
        if args:
            i = 0
            for ar in args:
                if i == 0:
                    self.id = ar
                elif i == 1:
                    self.width = ar
                elif i == 2:
                    self.height = ar
                elif i == 3:
                    self.x = ar
                elif i == 4:
                    self.y = ar
                i += 1
        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"id": self.id, "width": self.__width,
                "height": self.__height,
                "x": self.__x, "y": self.__y}
