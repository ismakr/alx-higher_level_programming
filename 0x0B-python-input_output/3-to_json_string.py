#!/usr/bin/python3
"""module: json"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""

    my_obj = json.dumps(my_obj)
    return my_obj
