#!/usr/bin/python3
"""
Summary
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
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
