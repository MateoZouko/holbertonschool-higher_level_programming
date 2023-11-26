#!/usr/bin/python3
"""
    This module contains the text_indentation function
    that it's tested on tests/5-text_indentation.txt

"""


def text_indentation(text):
    """Function that replaces . ? and : for \n\n"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new_text = text.replace(". ", ".\n\n")
    new_text = new_text.replace("? ", "?\n\n")
    new_text = new_text.replace(": ", ":\n\n")
    print(new_text, end='')
    