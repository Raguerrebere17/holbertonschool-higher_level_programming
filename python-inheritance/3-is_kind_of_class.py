#!/usr/bin/python3
""" 3-is_kind_of_class Module"""


def is_kind_of_class(obj, a_class):
    """ Function that returns True if the object is an instance of, \
        of if the object is an instance of a class that inherited from, \
            the specified class ; otherwise False."""
    return isinstance(obj, a_class)
