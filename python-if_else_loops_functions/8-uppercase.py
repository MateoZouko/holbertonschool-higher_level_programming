#!/usr/bin/python3
def uppercase(str):
    for char in str:
        ch = ord(char)
        if ch >= 97 and ch <= 122:
            ch -= 32
        print(chr(ch), end="")
    print()
