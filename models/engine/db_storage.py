#!/usr/bin/python3
"""
Contains the FileStorage class responsible for serialization and deserialization.
"""

import json
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

# Dictionary mapping class names to their respective classes
CLASSES_MAP = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
               "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    """Serializes instances to a JSON file and deserializes them back to instances."""

    # File path to store JSON data
    FILE_PATH = "file.json"
    # Dictionary to store serialized objects
    OBJECTS_DICT = {}

    def all(self, cls=None):
        """Return the dictionary of stored objects."""
        if not cls:
            return self.OBJECTS_DICT
        elif isinstance(cls, str):
            return {k: v for k, v in self.OBJECTS_DICT.items()
                    if v.__class__.__name__ == cls}
        else:
            return {k: v for k, v in self.OBJECTS_DICT.items()
                    if v.__class__ == cls}

    def new(self, obj):
        """Add a new object to the storage."""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.OBJECTS_DICT[key] = obj

    def save(self):
        """Serialize stored objects to the JSON file."""
        json_objects = {}
        for key in self.OBJECTS_DICT:
            json_objects[key] = self.OBJECTS_DICT[key].to_dict(save_to_disk=True)
        with open(self.FILE_PATH, 'w') as file:
            json.dump(json_objects, file)

    def reload(self):
        """Deserialize the JSON file and load objects into storage."""
        try:
            with open(self.FILE_PATH, 'r') as file:
                json_objects = json.load(file)
            for key in json_objects:
                self.OBJECTS_DICT[key] = CLASSES_MAP[json_objects[key]["__class__"]](**json_objects[key])
        except:
            pass

    def delete(self, obj=None):
        """Delete an object from storage if present."""
        if obj is not None:
            del self.OBJECTS_DICT[obj.__class__.__name__ + '.' + obj.id]
            self.save()

    def close(self):
        """Deserialize JSON file to objects."""
        self.reload()

    def get(self, cls, id):
        """Retrieve an object by class name and ID."""
        if cls is not None and isinstance(cls, str) and id is not None and \
                isinstance(id, str) and cls in CLASSES_MAP:
            key = cls + '.' + id
            obj = self.OBJECTS_DICT.get(key, None)
            return obj
        else:
            return None

    def count(self, cls=None):
        """Count the number of objects in storage."""
        total = 0
        if isinstance(cls, str) and cls in CLASSES_MAP:
            total = len(self.all(cls))
        elif cls is None:
            total = len(self.OBJECTS_DICT)
        return total
