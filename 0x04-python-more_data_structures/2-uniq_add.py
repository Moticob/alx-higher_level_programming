#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    num = 0

    iterator = iter(uniq_list)
    while True:
        try:
            i = next(iterator)
            num += i
        except StopIteration:
            break

    return (num)
