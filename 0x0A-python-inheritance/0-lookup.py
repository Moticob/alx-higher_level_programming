#!/usr/bin/python3
"""
up
"""


def lookup(obj):
    """
    Returns a list of available attribut.

    Args:
        obj: The object to inspect.

    Returns:
        A list containing the names of att.
    """
    return dir(obj)


if __name__ == "__main__":
    class MyClass1(object):
        """
        This is MyClass1, a simple class .
        """
        pass

    class MyClass2(object):
        """
        This is MyClass2, a class with an attribute my_att.
        """
        my_attr1 = 3
        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
