#!/usr/bin/python3
"""Define the City model for the HBNB project."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """The City class, containing state ID and name."""

    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

    def __init__(self, *args, **kwargs):
        """Initialize a new City."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.name = kwargs.get("name", "")
        self.state_id = kwargs.get("state_id", "")
