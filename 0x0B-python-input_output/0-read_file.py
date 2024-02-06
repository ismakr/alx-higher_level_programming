#!/usr/bin/python3
"""module: print file"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout"""

    with open(filename, "r") as fl:
        print(fl.read(), end="")
