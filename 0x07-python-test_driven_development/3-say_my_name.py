#!/usr/bin/python3
""""

This module is a function that prints a name

"""


def say_my_name(first_name, last_name=""):
    ''' prints name (<first name> <last name>)

    Args:
        first_name (str): The fisrt name
        last_name (str): The last name

    Raises:
        TypeError: If either the first_name and last_name are not strings

    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
