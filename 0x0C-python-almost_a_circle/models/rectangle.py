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
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__height * self.__width)

    def display(self):
        """Displays the rectangle using # """
        for y in range(self.y):
            print("")
        for row in range(self.__height):
            for x in range(self.x):
                print(" ", end="")
            for column in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Defines the string representation of the class"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}"
