#!/usr/bin/python3
"""python file that contains the class definition
of a State and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    States class

    Attributes:
    __tablename__ (str): The table's name
    id (int): The id primary key of the state
    name (str): The name of the state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name
