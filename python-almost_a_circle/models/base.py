#!/usr/bin/python3
"""
    Task 1: create a class called Base
"""


class Base:
    """
    Class Base created
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """
        Initialization setted
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
