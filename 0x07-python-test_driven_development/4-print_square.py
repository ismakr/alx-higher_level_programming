#!/usr/bin/python3
"""
module: print_square
"""


def print_square(size):
    """ function that prints a square with the character #."""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    i = 0
    while i < size:
        j = 0
        while j < size:
            print("#", end="")
            j += 1
        print("")
        i += 1


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
