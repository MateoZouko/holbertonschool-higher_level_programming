#!/usr/bin/python3
"""
    Task 10: And now, the Square!
    Defining a class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):

    """Represents a classs named square"""

    def __init__(self, size, x=0, y=0, id=None):
        """init a new method called Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """defining a new string method """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    @property
    def size(self):
        """Getter/setter the width of square"""
        return self.width

    @size.setter
    def size(self, value):
        """defining width and height"""
        self.width = value
        self.height = value
