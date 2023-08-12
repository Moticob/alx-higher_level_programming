#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    def get_values(t):
        if len(t) >= 1:
            yield t[0]
        else:
            yield 0
        if len(t) >= 2:
            yield t[1]
        else:
            yield 0

    a_values = list(get_values(tuple_a))
    b_values = list(get_values(tuple_b))

    new_tuple = tuple(a + b for a, b in zip(a_values, b_values))

    return new_tuple
