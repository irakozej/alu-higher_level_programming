#!/usr/bin/python3

def read_file(filename=""):
    """
    Read a text file (UTF8) and print its contents to stdout.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end='')

if __name__ == "__main__":
    read_file()  # Assuming the file name is provided as a command-line argument.
