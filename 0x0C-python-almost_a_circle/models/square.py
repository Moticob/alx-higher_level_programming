#!/usr/bin/python3
""" Square Module """
from models.rectangle import Rectangle

class Square(Rectangle):
    """ Square class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a new instance of the Square class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Return a string representation of the Square object """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
