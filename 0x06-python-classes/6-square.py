#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square by:
        Private instance attribute: size"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size == 0:
            print("")
            return
        t = 0
        i = 0
        while t < self.__position[1]:
            print("")
            t += 1
        while i < self.__size:
            k = 0
            j = 0
            while k < self.__position[0]:
                print(" ", end="")
                k += 1
            while j < self.__size:
                print("#", end="")
                j += 1
            print("")
            i += 1
