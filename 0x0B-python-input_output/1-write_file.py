#!/usr/bin/python3
"""
up
"""


def number_of_lines(filename=""):
    """ return the number of lines of a file """
    i = 0
    with open(filename, encoding='utf-8') as file:
        for line in file:
            i += 1
    return i
