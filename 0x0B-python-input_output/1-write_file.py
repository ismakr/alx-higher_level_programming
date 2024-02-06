#!/usr/bin/python3
"""module: write to file"""


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, "w") as fl:
        return fl.write(text)
