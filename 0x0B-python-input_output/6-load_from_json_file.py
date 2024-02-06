#!/usr/bin/python3
"""json_obj"""
import json


def load_from_json_file(filename):
    """ creates an Object from a “JSON file”"""

    with open(filename, "r") as fl:
        return json.loads(fl.read())
