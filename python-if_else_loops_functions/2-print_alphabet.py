#!/usr/bin/python3
# 2-print_alphabet.py

"""Printing the alphabets in lowercase, with no new line."""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
