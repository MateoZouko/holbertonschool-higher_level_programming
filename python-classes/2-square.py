#!/usr/bin/python3
""" This module define a class Square """


class Square():
    """ This class define a Square """
    __size = None

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
