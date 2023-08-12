#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    index = 0
    first_char = None

    while index < len_sen and first_char is None:
        first_char = sentence[index]
        index += 1

    new_tuple = (len_sen, first_char)

    return new_tuple
