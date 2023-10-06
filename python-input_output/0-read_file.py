#!/usr/bin/python3
"""
Write a function that reads a text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    defining read file function
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
