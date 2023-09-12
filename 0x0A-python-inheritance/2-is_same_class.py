#!/usr/bin/python3
"""Checks if object is an instance"""


def is_same_class(obj, a_class):
    """Return true if object is an instance of the
    class, otherwise return false
    """
    return (type(obj) == a_class)
