#!/usr/bin/python3
"""Module for defining the Review class in the HBNB project"""

from os import getenv
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey


class Review(BaseModel, Base):
    """Represents a review object."""

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'reviews'
        review_text = Column(String(60),
                             nullable=False)
        place_id = Column(String(60),
                          ForeignKey('places.id'),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id'),
                         nullable=False)
    else:
        place_id = ""
        user_id = ""
        review_text = ""

    def __init__(self, *args, **kwargs):
        """Initialize a review instance."""
        super().__init__(*args, **kwargs)
