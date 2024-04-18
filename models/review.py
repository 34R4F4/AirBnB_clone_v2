#!/usr/bin/python3
"""Define the Review model for the HBNB project."""
from sqlalchemy import Column, ForeignKey, String
from models.base_model import Base, BaseModel


class Review(BaseModel, Base):
    """Review class to store review information."""

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initialize a new Review."""
        filtered_kwargs = {k: v for k, v in kwargs.items()
                           if hasattr(self, k) or k == "id"}
        super().__init__(*args, **filtered_kwargs)
        self.text = kwargs.get("text", "")
        self.user_id = kwargs.get("user_id", "")
        self.place_id = kwargs.get("place_id", "")
