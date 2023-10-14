#!/usr/bin/python3
"""
    Task 1: create a class called Base
"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) <= 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        with open(f"{cls.__name__}.json", "w") as f:
            if list_objs is None or len(list_objs) == 0:
                f.write(cls.to_json_string(None))
            else:
                result = []
                for obj in list_objs:
                    result.append(obj.to_dictionary())
                f.write(cls.to_json_string(result))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return "[]"
        if len(json_string) == 0:
            "[]"
        return json.loads(json_string)
