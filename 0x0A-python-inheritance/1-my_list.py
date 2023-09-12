#!/usr/bin/python3
"""Inherits from the list class"""


class MyList(list):
    """class inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
