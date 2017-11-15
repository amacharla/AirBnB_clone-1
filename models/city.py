#!/usr/bin/python
""" holds class City"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Representation of city """

    __tablename__ = "cities"
    state_id = Column(String(60), nullable=False, ForeignKey="states.id")
    name = Column(String(128), nullable=False)

    places = relationship("Place", backref="cities")

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
