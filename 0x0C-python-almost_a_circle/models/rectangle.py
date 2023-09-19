#!/usr/bin/python3
"""Contains a rectangle class"""

from models.base import Base


class Rectangle(Base):
    """ A rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes attributes"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # List of getter functions
    @property
    def width(self):
        """Gets the width"""
        return self.__width

    @property
    def height(self):
        """Gets the height"""
        return self.__height

    @property
    def x(self):
        """Gets the x"""
        return self.__x

    @property
    def y(self):
        """Gets the y"""
        return self.__y

    # List of setter functions
    @width.setter
    def width(self, value):
        """Sets the width"""
        if (type(value) is not int):
            raise TypeError("width is not an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height"""
        if (type(value) is not int):
            raise TypeError("height is not an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x"""
        if (type(value) is not int):
            raise TypeError("x is not an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y"""
        if (type(value) is not int):
            raise TypeError("y is not an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
