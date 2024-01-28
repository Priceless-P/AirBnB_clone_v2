#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import os
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return self.__objects
        else:
            if type(cls) is str:
                cls = eval(cls)
            clss = {}
            for key, value in self.__objects.items():
                if type(value) is cls:
                    clss[key] = value
            return clss

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(self.__file_path, 'w') as f:
            temp = {}
            temp.update(self.__objects)
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
                    'BaseModel': BaseModel, 'Place': Place, 'User': User,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            if os.path.getsize(self.__file_path) > 0:
                with open(self.__file_path, 'r') as f:
                    temp = json.load(f)
                    for key, val in temp.items():
                        self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if its inside"""
        if obj is not None:
            key = str(obj.__class__.__name__) + "." + str(obj.id)
            del self.__objects[key]
            self.save()
        else:
            return

    def close(self):
        """Reset the use of data"""
        self.reload()
