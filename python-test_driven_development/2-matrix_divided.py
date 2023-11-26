#!/usr/bin/python3
"""
    This module defines an divide matrix function
    and it's tested on /tests folder.

"""


def matrix_divided(matrix, div):
    """
    Divides each element of the matrix by div
    """
    if (not isinstance(matrix, list)) or (not isinstance(matrix[0], list)):
        raise TypeError("must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if int(div) == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    for row in matrix:
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("must be a matrix (list of lists) \
                   of integers/floats")
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)
    return new_matrix
