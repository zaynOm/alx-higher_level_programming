#!/usr/bin/python3
"City model"

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    "Declarative city model"
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
