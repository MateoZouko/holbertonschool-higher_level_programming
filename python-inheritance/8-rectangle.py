#!/usr/bin/python3

"""
Task 8
"""


class BaseGeometry:
    """
    Clase BaseGeometry definida
    """
    def area(self):
        """
        defining area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        defining integrer validator
        """
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Defining Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        initializing
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
