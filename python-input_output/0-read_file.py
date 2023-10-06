#!/usr/bin/python3
"""
    Task 0: Read File
    Write a function that reads a
    text file (UTF8) and prints it to stdout:
"""


def read_file(filename=""):
    """
    defining a function that reads
    file and prints its content
    """
    with open(filename, 'r', encoding="utf-8") as file:
        input = file.read()
        print(input, end="")
