#!/usr/bin/python3
"""Define a class square."""

class Square:
    """This is square class"""

    def __init__(self, size=0):

         """
        Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if not isinstance(size, int):
            Raise TypeError("size has to be of int type")

            elif size < 0:
                Raise ValueError("size must be greater than 0")
             self.__size=size

                def area(self):
              """Return area of square"""
              return (self.__size*self.__size)
