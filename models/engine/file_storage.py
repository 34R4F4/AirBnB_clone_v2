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
        """Return a list of objects of one type of class (optional filtering).

         Args:
            cls (optional): The class type to filter objects by. If provided, only objects
                of the specified class type will be included in the returned list.

        Returns:
            list: A list of objects filtered by the specified class type, or all objects
                if no class type is specified.

        """
        # If cls is not provided, return all objects in the storage
        if cls is None:
            return list(self.__objects.values())
        # Filter objects by the specified class type
        return [obj for obj in self.__objects.values() if isinstance(obj, cls)]

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
