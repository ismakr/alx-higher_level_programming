#!/usr/bin/python3
"""module: student"""


class Student():
    """class Student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation
        of a Student instance"""
        if isinstance(attrs, list):
            lidic = {k: self.__dict__[k] for k in attrs if k in self.__dict__}
            return lidic
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance"""
        for k, v in json.items():
            if k in self.__dict__:
                self.__dict__[k] = v
