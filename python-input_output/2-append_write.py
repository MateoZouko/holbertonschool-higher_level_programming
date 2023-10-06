#!/usr/bin/python3
"""
Write a function that writes a string
to a text file (UTF8) and returns
the number of characters written:
"""


def append_write(filename="", text=""):
    """defining a function that writes
    to a txt file and return the numbre
    of charachters in it."""

    with open(filename, 'a', encoding='utf-8') as file:
        characters = file.write(text)
        return characters
