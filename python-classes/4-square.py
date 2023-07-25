#!/usr/bin/python3
"""This is module documentation"""



class Square:
    """This is class module"""

    
    def __init__(self, size = 0):
        """initialize size variable.


        Args:
        size(int):The size of the new square
        """
        self.size = size
        @property
        def size(self):
            """get and set size of square."""

        return (self.__size)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            Raise ValueError("sixe muzt be greater than 0")
            self.__size = value

            def area(self):
                """here we return the area of square"""
                return (self.__size*self.__size)

