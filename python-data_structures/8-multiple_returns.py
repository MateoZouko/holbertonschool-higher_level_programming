#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        character = sentence[0]
        tuple_new = (length, character)
        return tuple_new
    length = len(sentence)
    tuple_new = (length, None)
    return tuple_new
