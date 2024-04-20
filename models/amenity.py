#!/usr/bin/python3
"""Define the Amenity class."""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Representation of an Amenity."""

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)
    place_amenities = relationship(
            "Place", secondary="place_amenity", backref="amenities")

    def __init__(self, *args, **kwargs):
        """Initialize Amenity."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.name = kwargs.get("name", "")
