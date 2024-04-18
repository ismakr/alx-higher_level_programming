#!/usr/bin/python3
"""contains the class definition of a City"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
Base = declarative_base()


class City(Base):
    """links to the MySQL table cities"""
    __tablename__ = 'cities'
    id = Column(Integer,  primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(ForeignKey(State.id), nullable=False)
