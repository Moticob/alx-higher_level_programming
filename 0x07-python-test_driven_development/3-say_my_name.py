#!/usr/bin/python3
"""
    Insert here module comment

    Write a function that prints My name is <first name> <last name>

    Prototype: def say_my_name(first_name, last_name=""):
    first_name and last_name must be strings otherwise,
    raise a TypeError exception with the message
    first_name must be a string or last_name must be a string
    You are not allowed to import any module

"""



def say_my_name(first_name, last_name=""):
    """
    Prints a formatted string with the provided first name and last name.

    Args:
        first_name (str): The first name to be printed.
        last_name (str, optional): The last name to be printed. Defaults to an empty string.

    Raises:
        TypeError: If either `first_name` or `last_name` is not a string.

    Example:
        >>> say_my_name("John", "Smith")
        My name is John Smith

        >>> say_my_name("Walter", "White")
        My name is Walter White

        >>> say_my_name("Bob")
        My name is Bob

        >>> say_my_name(12, "White")
        Traceback (most recent call last):
            ...
        TypeError: first_name must be a string or last_name must be a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    full_name = f"My name is {first_name} {last_name}" if last_name else f"My name is {first_name}"
    print(full_name)

# Test cases
if __name__ == "__main__":
    say_my_name("John", "Smith")
    say_my_name("Walter", "White")
    say_my_name("Bob")
    try:
        say_my_name(12, "White")
    except TypeError as e:
        print(e)
