#!/usr/bin/python3
"""json_file"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""

    with open(filename, "a") as fl:
        json.dump(my_obj, fl)
