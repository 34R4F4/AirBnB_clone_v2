#!/usr/bin/python3
"""Defines the User class."""

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """Representation of a user."""

    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")

    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.email = kwargs.get("email", "")
        self.password = kwargs.get("password", "")
        self.first_name = kwargs.get("first_name", "")
        self.last_name = kwargs.get("last_name", "")
