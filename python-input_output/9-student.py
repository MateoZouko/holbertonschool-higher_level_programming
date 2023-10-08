#!/usr/bin/python3

"""
    Defining a class called Student
"""


class Stundent:
    """
    Defining Student class with fist_name,
    last_age and age
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_age = last_name
        self.age = age

    def to_json(self):
        return self.__dict__