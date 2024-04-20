#!/usr/bin/python3
"""Define the State model for the HBNB project."""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """State class."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # Define relationship based on storage type
    if models.storage_type == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter attribute for cities."""
            cities = models.storage.all(City)
            return [city for city in cities.values()
                    if city.state_id == self.id]

    def __init__(self, *args, **kwargs):
        """Initialize a new State."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.name = kwargs.get("name", "")
