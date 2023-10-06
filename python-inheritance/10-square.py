#!/usr/bin/python3

"""
This module contains the class 'Square'
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    setting class
    """
    def __init__(self, size=0):
        """
        defining init
        """
        super().__init__(size, size)
