#!/usr/bin/python3
"""this is 1 line creating a class"""


class Square:
    """we are inside the class"""

    def __init__(self, size = 0):
        """this is the instance of size

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an interger")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
