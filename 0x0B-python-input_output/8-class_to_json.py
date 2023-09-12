#!/usr/bin/python3
""" defines a Python class-to-JSON """


def class_to_json(obj):
    """Returns the dictionary representation"""
    return obj.__dict__
