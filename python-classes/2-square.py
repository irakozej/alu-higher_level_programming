#!/usr/bin/python3
"""
This module defines the Square class
"""



class Square:


    """
    this is class boddy
    """


    def __init__(self, size=0):
        """decralation and  initializing class variables


Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            """
            if not isinstance(size, int):
                RaiseTypeError("size must be an integer")

                if size < 0:
                    RaiseTypeError("size ust be positive")
                    self.__size = size
