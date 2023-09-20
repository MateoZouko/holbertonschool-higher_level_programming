#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            uppercase_char = chr(char_code - 32)
        else:
            uppercase_char = char
        print(uppercase_char, end="")

    print()
