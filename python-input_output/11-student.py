#!/usr/bin/python3

"""
    Module defining a class called Student
"""


class Student:
    """
    Defining Student class with fist_name,
    last_name and age
    """
    def __init__(self, first_name, last_name, age):
        """defining initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """defining new function"""
        if type(attrs) is list:
            if all(isinstance(item, str) for item in attrs):
                clasDict = dict(self.__dict__)
                filt_dict = {a: b for (a, b) in clasDict.items() if a in attrs}
                return filt_dict
        return self.__dict__

    def reload_from_json(self, json):
        """defining new function"""
        for (a, b) in json.items():
            clasDict = dict(self.__dict__)
            clasDict.update(json)
            self.__dict__ = clasDict
