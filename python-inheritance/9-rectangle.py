#!/usr/bin/python3

"""
Task 9
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

    def area(self):
        """
        defining area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        defining __str__
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
