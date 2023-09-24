#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence:
        length = len(sentence)
        letter = sentence[0]
        return(length, letter)
    return None
