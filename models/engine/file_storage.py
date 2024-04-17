#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        file_path (str): The path to the JSON file used for storage.
        objects (dict): A dictionary holding instantiated objects.
        all_classes (dict): A dictionary mapping class names to their corresponding classes.
    """

    file_path = "file.json"
    objects = {}
    all_classes = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self, cls=None):
        """
        Returns a dictionary of all or filtered objects.

        Args:
            cls (str, optional): The class type to filter by. Defaults to None (all objects).

        Returns:
            dict: A dictionary containing requested objects.
        """

        all_objects = {}

        # Check if a valid class is provided for filtering
        if cls:
            if cls.__name__ in self.all_classes:
                # Filter objects by class type
                for key, val in self.objects.items():
                    if key.split('.')[0] == cls.__name__:
                        all_objects.update({key: val})
        else:
            # Return all objects if no class filter is provided
            all_objects = self.objects

        return all_objects

    def new(self, obj):
        """
        Adds a new object to the internal objects dictionary.

        Args:
            obj (object): The object to add.
        """

        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.objects[key] = obj

    def save(self):
        """
        Serializes the objects dictionary to a JSON file.
        """

        serialized_objects = {}
        for key, value in self.objects.items():
            serialized_objects[key] = value.to_dict()

        with open(self.file_path, 'w', encoding="UTF-8") as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """
        Attempts to deserialize the JSON file and load objects into memory.

        Ignores any errors if the file doesn't exist.
        """

        try:
            with open(self.file_path, 'r', encoding="UTF-8") as f:
                loaded_dict = json.load(f)
                for key, value in loaded_dict.items():
                    class_name = value["__class__"]
                    del value["__class__"]  # Remove metaclass information
                    self.objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass

    def close(self):
        """
        Reloads objects from the JSON file (if it exists).
        """

        self.reload()

    def delete(self, obj=None):
        """
        Deletes an object from the internal objects dictionary, if it exists.

        Args:
            obj (object, optional): The object to delete. Defaults to None.
        """

        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            del self.objects[key]
