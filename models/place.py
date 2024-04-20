#!/usr/bin/python3
"""Define the Place model for the HBNB project."""
import models
from models.base_model import BaseModel, Base
from models.review import Review
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import environ

place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column("place_id", String(60), ForeignKey("places.id")),
    Column("amenity_id", String(60), ForeignKey("amenities.id"))
)


class Place(BaseModel, Base):
    """A place to stay."""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if environ.get("HBNB_ENV") == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 backref="place_amenities", viewonly=False)
    else:
        @property
        def reviews(self):
            """Get all reviews related to the place."""
            return [o for o in models.storage.all(Review)
                    if o.place_id == self.id]

        @property
        def amenities(self):
            """Get all amenities related to the place."""
            return [o for o in models.all(Amenity)
                    if o.place_id == self.id]

        @amenities.setter
        def amenities(self, obj):
            """Set amenities related to the place."""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)

    def __init__(self, *args, **kwargs):
        """Initialize a new Place."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.number_rooms = kwargs.get("number_rooms", 0)
        self.number_bathrooms = kwargs.get("number_bathrooms", 0)
        self.max_guest = kwargs.get("max_guest", 0)
        self.price_by_night = kwargs.get("price_by_night", 0)
        self.city_id = kwargs.get("city_id", "")
        self.user_id = kwargs.get("user_id", "")
