#!/usr/bin/python3
"""this is 1 line creating a class"""


class Square:
    """we are inside the class"""

    def __init__(self, size=0, position=(0,0)):
        """this is the instance of size

        Args:
            size (int): The size of the new square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """gets curent size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the square area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints the square"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range (self.__size)]
            print("")
        if self.__size == 0:
            print("")
            return
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")
