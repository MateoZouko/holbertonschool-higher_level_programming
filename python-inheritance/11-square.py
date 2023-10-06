#!/usr/bin/python3

"""
This module contains the class 'Square'
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    setting class
    """
    def __init__(self, size):
        """
        defining init
        """
        super().__init__(size, size)

    def __str__(self):
        """
        defining __str__
        """
        return f"[Square] {self._Rectangle__width}/{self._Rectangle__height}"
