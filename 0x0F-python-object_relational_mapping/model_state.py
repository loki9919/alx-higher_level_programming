#!/usr/bin/python3
"""
file that contains the class definition of a State and
an instance Base = declarative_base()
"""
from sys import argv
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    """ class with id and name attributes of each state """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
