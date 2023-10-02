#!/usr/bin/python3
""" This module define a class Square """


class Square:
    """ This class define a Square """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ Getter method to retrieve the size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method to set the size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Calculate and return area """
        return self.__size ** 2
