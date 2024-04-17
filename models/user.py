#!/usr/bin/python3
"""Module for defining the User class in the HBNB project"""

import hashlib
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class User(BaseModel, Base):
    """Represents a user object."""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'users'
        email = Column(String(128),
                       nullable=False)
        hashed_password = Column('password',
                                 String(128),
                                 nullable=False)
        first_name = Column(String(128),
                            nullable=True)
        last_name = Column(String(128),
                           nullable=True)
        places = relationship("Place",
                              backref="user",
                              cascade="all, delete-orphan")
        reviews = relationship("Review",
                               backref="user",
                               cascade="all, delete-orphan")
    else:
        email = ""
        hashed_password = ""
        first_name = ""
        last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a user instance."""
        super().__init__(*args, **kwargs)

    @property
    def password(self):
        """Getter method for password."""
        return self.hashed_password

    @password.setter
    def password(self, pwd):
        """Setter method for password."""
        self.hashed_password = pwd
