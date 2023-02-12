#!/usr/bin/python3

"""Convert the dictionary representation to a JSON string"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}
    class_map = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                 "City": City, "Place": Place, "State": State,
                 "Review": Review}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as f:
            for value in all_dict.values():
                key = f"{value.__class__.__name__}.{value.id}"
                ser_dict[key] = value.to_dict()
            json.dump(ser_dict, f)

    def reload(self):
<<<<<<< HEAD
        """Deserializes the JSON file to __objects (only if the JSON file (__file_path) exists,
        otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
=======
        """Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists,
        otherwise, do nothing. If the file doesn’t exist
        , no exception should be raised)"""
>>>>>>> 3d6a52a032bbdbccd46fd1a87bf94848f25f9d4c
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                des_json = json.load(f)
                for key, value in des_json.items():
                    class_name, _, obj_id = key.rpartition(".")
                    obj_class = self.class_map.get(class_name)
                    if obj_class:
                        self.new(obj_class(**value))
