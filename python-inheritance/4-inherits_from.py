#!/usr/bin/python3
""" module: 4-inherts_from"""


def inherts_from(obj, a_class):
    """the object is an inherited class
    obj: an object
    a_class: a class
    returns None
    """
    return type(obj) != a_class and isinstance(obj, a_class)