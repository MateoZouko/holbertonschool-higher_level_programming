#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        new_tuple = (tuple_a[0], 0)
    else:
        new_tuple = tuple_a[:2]

    if len(tuple_b) == 0:
        new_tuple2 = (0, 0)
    elif len(tuple_b) < 2:
        new_tuple2 = (tuple_b[0], 0)
    else:
        new_tuple2 = tuple_b[:2]

    result = (new_tuple[0] + new_tuple2[0], new_tuple[1] + new_tuple2[1])
    return result
