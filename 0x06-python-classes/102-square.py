#!/usr/bin/python3
""" class Square that defines aupp   square"""


class Square:
    """
    This class represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        self.__size = 0  # Initialize with default value
        self.size = size  # Use property setter to set the size

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not a number.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Less than comparator for square instances based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area of self is less than the area of other, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparator for square instances based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area of self is .
        """
        return self.area() <= other.area()

    def __eq__(self, other):
        """
        Equal to comparator for square instances based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area of self is equal to the .
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Not equal to comparator for square instances based on area.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area of self is not equal to th.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Greater than comparator for square insta.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area of self is great.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparator for square.

        Args:
            other (Square): Another Square instance.

        Returns:
            bool: True if the area of self is greate.
        """
        return self.area() >= other.area()


# Test the class
if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
