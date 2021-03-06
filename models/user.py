#!/usr/bin/python3
""" holds class User"""
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os
import models


class User(BaseModel, Base):
    """Representation of a user """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship('Place', cascade='all, delete', backref='user')
        reviews = relationship('Review', cascade='all, delete', backref='user')
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""

        def __init__(self, *args, **kwargs):
            """initializes user"""
            super().__init__(*args, **kwargs)
