#!/usr/bin/python3
"""Module for defining the State class in the HBNB project"""

import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """Represents a state object."""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        state_name = Column(String(128),
                            nullable=False)
        cities = relationship("City", cascade="all, delete",
                              backref="states")
    else:
        state_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a state instance."""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """FileStorage getter attribute that returns City instances."""
            values_city = models.storage.all("City").values()
            list_city = []
            for city in values_city:
                if city.state_id == self.id:
                    list_city.append(city)
            return list_city
