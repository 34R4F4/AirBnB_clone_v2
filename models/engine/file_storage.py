#!/usr/bin/python3
"""Class for managing file storage for hbnb clone."""

import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Manage storage of hbnb models in JSON format."""

    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of models currently in storage."""
        objects = FileStorage.__objects
        if cls is None:
            return objects
        return {key: value for (key, value) in objects.items()
                if key.startswith(cls.__name__ + '.')}

    def new(self, obj):
        """Add a new object to the storage dictionary."""
        self.__objects.update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Save the storage dictionary to file."""
        with open(FileStorage.__file_path, 'w') as file:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, value in temp.items():
                temp[key] = value.to_dict()
            json.dump(temp, file)

    def reload(self):
        """Load the storage dictionary from file."""
        classes = {'BaseModel': BaseModel, 'User': User, 'Place': Place,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Review': Review}
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as file:
                temp = json.load(file)
                for key, value in temp.items():
                    self.all()[key] = classes[value['__class__']](**value)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a parameter object from __objects."""
        if obj is None:
            return
        del FileStorage.__objects[obj.to_dict()['__class__'] + '.' + obj.id]
