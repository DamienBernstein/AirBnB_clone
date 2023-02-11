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
    FILE_PATH = "file.json"
    OBJECTS = {}
    LABEL_DICT = {
        "BaseModel": BaseModel,
        "User": User,
        "Amenity": Amenity,
        "City": City,
        "Place": Place,
        "State": State,
        "Review": Review
    }

    def all(self):
        return self.OBJECTS

    def new(self, obj):
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.OBJECTS[key] = obj

    def save(self):
        serialized_dict = {}
        for value in self.OBJECTS.values():
            key = "{}.{}".format(type(value).__name__, value.id)
            serialized_dict[key] = value.to_dict()
        
        with open(self.FILE_PATH, 'w') as f:
            json.dump(serialized_dict, f)

    def reload(self):
        if os.path.isfile(self.FILE_PATH):
            with open(self.FILE_PATH, 'r') as f:
                deserialized_json = json.load(f)
                for key, value in deserialized_json.items():
                    class_name, _, obj_id = key.rpartition('.')
                    cls = self.LABEL_DICT.get(class_name)
                    if cls:
                        obj = cls(**value)
                        obj.id = obj_id
                        self.new(obj)
