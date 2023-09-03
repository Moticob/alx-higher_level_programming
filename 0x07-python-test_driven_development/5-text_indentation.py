#!/usr/bin/python3
"""
    Insert here module comment

    Write a function that prints a text with 2 new lines
    after each of these characters: ., ? and :

    Prototype: def text_indentation(text):

    text must be a string, otherwise raise a TypeError
    exception with the message text must be a string
    There should be no space at the beginning or at the
    end of each printed line so that you don’t miss any
    edge case

"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If `text` is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text using the specified characters as delimiters
    parts = text.split('. ')
    parts = [part.strip() for part in parts]  # Remove leading/trailing spaces

    # Join the parts with the specified characters plus two new lines
    formatted_text = '.\n\n'.join(parts)

    # Print the formatted text
    print(formatted_text)
