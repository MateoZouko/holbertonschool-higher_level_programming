#!/usr/bin/python3

"""
Task 8
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Defining Rectangle class
    """
    def __init__(self, width, height):
        """
        initializing
        """
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
