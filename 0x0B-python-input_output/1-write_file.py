#!/usr/bin/env python3
"""
Writes a string to a text file (UTF8) and returns the character count.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns character count.
    
    Args:
        filename (str): The name of the file to write to.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)


if __name__ == "__main__":
    nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
    print(nb_characters)
