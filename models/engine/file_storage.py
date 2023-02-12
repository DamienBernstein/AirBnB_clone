#!/usr/bin/python3
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
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        with open(FileStorage.__file_path, 'w') as f:
            obj_dict = {}
            for key, value in FileStorage.__objects.items():
                obj_dict[key] = value.to_dict()
            f.write(json.dumps(obj_dict))

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                obj_dict = json.loads(f.read())
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split(".")
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        FileStorage.__objects[key] = User(**value)
                    elif class_name == "Place":
                        FileStorage.__objects[key] = Place(**value)
                    elif class_name == "State":
                        FileStorage.__objects[key] = State(**value)
                    elif class_name == "City":
                        FileStorage.__objects[key] = City(**value)
                    elif class_name == "Amenity":
                        FileStorage.__objects[key] = Amenity(**value)
                    elif class_name == "Review":
                        FileStorage.__objects[key] = Review(**value)
        except:
            pass

