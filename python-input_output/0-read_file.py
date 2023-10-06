#!/usr/bin/python3
"""
    Task 0: Read File
"""


def read_file(filename=""):
    """
    defining read file function
    """
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file.read():
            print(line, end="")
