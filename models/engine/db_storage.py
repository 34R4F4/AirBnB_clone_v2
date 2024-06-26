#!/usr/bin/python3
"""Module for DBStorage class."""

from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
import os

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """Class for managing database storage."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the class."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                      os.environ.get("HBNB_MYSQL_USER"),
                                      os.environ.get("HBNB_MYSQL_PWD"),
                                      os.environ.get("HBNB_MYSQL_HOST"),
                                      os.environ.get("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if os.environ.get("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query the current database session."""
        if cls is None:
            classes = [User, State, City, Amenity, Place, Review]
            objects = []
            for class_obj in classes:
                objects += self.__session.query(class_obj).all()
        else:
            objects = self.__session.query(cls).all()
        return {type(obj).__name__ + "." + obj.id: obj
                for obj in objects}

    def new(self, obj):
        """Add the object to the current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
