#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    multiply = lambda i: i * number
    return (list(map(multiply, my_list)))
