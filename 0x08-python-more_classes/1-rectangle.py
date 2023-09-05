#!/usr/bin/python3
"""A class for a rectangle"""


class Rectangle:
    """this is a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing rectangle class
        Args:
            width: the width of the rectangle
            height: the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
