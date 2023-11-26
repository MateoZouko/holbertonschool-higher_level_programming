#!/usr/bin/python3


"""
Task 0:
defines an add function
    and it's tested on /tests folder.
"""


def add_integer(a, b=98):
    """
a and b must be integers or floats, otherwise raise
a TypeError exception with the message a must be an
integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)) or \
       not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("a must be an integer or b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
