#!/usr/bin/python3

"""
Module: append_write.py

module that return the number of characters added.
"""


def append_write(filename="", text=""):


    """
Add a string and return the number of characters added.

    Args:
    filename (str): The name of the file to which the text will be added.
        text (str): The string to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    text = input("Enter the text to append: ")

    num_chars_added = append_write(filename, text)
    print(f"{num_chars_added} characters were added to {filename}.")
