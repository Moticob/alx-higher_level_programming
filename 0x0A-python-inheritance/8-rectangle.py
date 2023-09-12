#!/usr/bin/python3
"""up"""


class BaseGeometry:
    """BaseGeometry class."""
    def area(self):
        """Raises Exception: area() is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate 'value': int, positive."""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""
    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
