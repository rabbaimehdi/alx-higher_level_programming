#!/usr/bin/python3
""" defines a text reading function"""


def read_file(filename=""):
    """Prints the contents of a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
