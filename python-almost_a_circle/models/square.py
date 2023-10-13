#!/usr/bin/python3
"""
    Task 10: And now, the Square!
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            width (int): The width of the new square.
            height (int): The height of the new square.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
            defining __str__
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
