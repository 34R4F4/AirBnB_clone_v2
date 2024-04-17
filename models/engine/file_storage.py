#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'Place': Place, 'City': City,
                   'Amenity': Amenity, 'Review': Review}

    def all(self, cls=None):
        """
        eturns the list of objects of one type of class.

        Parameters:
            cls (class, optional): The class type to filter objects.
                Default: None.

         Returns:
            dict: A dictionary containing objects of the specified class type,
                or all objects if no class type is provided.
        """

       return_dict = {}

       # If cls is provided, filter objects accordingly
        if cls:
            class_name = cls.__name__
            if class_name in self.all_classes:
                return_dict.update(
                        {key: val for key, val in self.__objects.items()
                            if key.split('.')[0] == class_name})
        else:
            # If cls is None, return all objects
            return_dict = self.__objects.copy()

        return return_dict
        

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass


    def delete(self, obj=None):
        """
        Deletes an object from __objects if it exists.

        Parameters:
            obj (BaseModel, optional): The object to be deleted.
                Defaults: None.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects.pop(key, None)
