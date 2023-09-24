#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i, element in enumerate(line):
            if i == len(line) - 1:
                print("{}".format(element), end='')
            else:
                print("{} ".format(element), end='')
        print()
