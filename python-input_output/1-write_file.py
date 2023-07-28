#!/usr/bin/python3

"""
Module: write_file.py

This module provides a function to write a string to a text file (UTF8) and return the number of characters written.
"""

def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The string to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

if __name__ == "__main__":
    filename = input("Enter the filename: ")
    text = input("Enter the text to write: ")

    num_chars_written = write_file(filename, text)
    print(f"{num_chars_written} characters were written to {filename}.")
