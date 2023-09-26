#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_dictionary = sorted(a_dictionary.keys())
    for key in sorted_dictionary:
        value = a_dictionary[key]
        print(f"{key}: {value}")
