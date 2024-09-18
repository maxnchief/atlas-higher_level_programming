#!/usr/bin/python3

"""defines class checking function"""


def is_same_class(obj, a_class):
    """checks if there is another instance of the same class
    Args:
        obj (any): the object to check
        a_class (type): The class to compare against
    Returns:
        if the obj is an exact match - True
        else - False
    """

    if type(obj) == a_class:
        return True
    return False
