#!/usr/bin/python3
"""base class mod"""
import json


class Base:
    """class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(f"{cls.__name__}.json", "w") as fl:
            if list_objs is None:
                fl.write("[]")
            else:
                dic_li = [i.to_dictionary() for i in list_objs]
                fl.write(Base.to_json_string(dic_li))
