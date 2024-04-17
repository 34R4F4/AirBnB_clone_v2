#!/usr/bin/python3
"""Creates a unique storage instance for the application"""

from os import environ
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


# Check environment variable to determine storage method
if environ['HBNB_TYPE_STORAGE'] == 'db':
    from models.engine.db_storage import DBStorage
    storage_instance = DBStorage()
    storage_instance.reload()

else:  # File storage selected
    from models.engine.file_storage import FileStorage
    storage_instance = FileStorage()
    storage_instance.reload()
