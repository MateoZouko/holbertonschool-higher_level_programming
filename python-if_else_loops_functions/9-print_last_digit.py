#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_digit = number % 10
    else:
        positive = number * -1
        last_digit = positive % 10

    print(last_digit, end="")
    return last_digit
