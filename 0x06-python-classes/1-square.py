#!/usr/bin/python3
"""
This module defines a class Square.
"""

class Square:
    """
    A class to represent a square.

    Attributes:
        __size (int): The size of the square (private).
    """
    def __init__(self, size):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
