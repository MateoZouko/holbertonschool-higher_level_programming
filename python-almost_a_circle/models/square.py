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

    def update(self, *args, **kwargs):
        """defining update args for square"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """creating a new dictionary"""

        return{
           'id': self.id,
           'width': self.width,
           'height': self.height,
           'x': self.x,
           'y': self.y
        }
