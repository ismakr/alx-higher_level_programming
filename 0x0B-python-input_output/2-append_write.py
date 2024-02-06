#!/usr/bin/python3
"""module: append file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added"""

    with open(filename, "a") as fl:
        return fl.write(text)
