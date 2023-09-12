#!/usr/bin/python3
"""
up
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    """
    def print_sorted(self):
        """
        Print the list in ascending order.
        """
        print(sorted(self))
