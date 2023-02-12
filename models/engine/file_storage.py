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

# models/engine/file_storage.py
import json
from models.base_model import BaseModel
from models.user import User




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
        except:
            pass
