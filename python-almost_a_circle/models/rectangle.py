#!/usr/bin/python3
"""
    Task 2: Class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Represent a rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Get/set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """
            Get/set the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self,value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self,value):
        self.__y = value
