#!/usr/bin/python3
import json
"""module: str-json"""


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string"""

    my_str = json.loads(my_str)
    return my_str
