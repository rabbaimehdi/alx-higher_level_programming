#!/usr/bin/python3
""" defines a class Student"""


class Student:
    """ a student."""

    def __init__(self, first_name, last_name, age):
        """ a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation"""
        return self.__dict__
