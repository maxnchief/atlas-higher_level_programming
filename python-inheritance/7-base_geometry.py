#!/usr/bin/python3
"""
this is a base basegeometry class

"""


class BaseGeometry:
    """
    Class: BaseGeometry
    """
    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validats perameters
        Args:
            name (str): name of parameter
            value (int): the parameter to validate
        Raises:
            TypeError: Value is not an interger
            ValueError: Value is <=0
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
