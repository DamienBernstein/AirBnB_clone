#!/usr/bin/python3 


""" Convert the dictionary representation to a JSON string """
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
    """
    Class that serializes instances to a JSON file and deserializes
    JSON file to instances
    """

    # Define the file path for the JSON file
    __file_path = "file.json"
    # Dictionary to store the objects
    __objects = {}
    # Mapping of class names to their respective classes
    class_dict = {"BaseModel": BaseModel, "User": User, "Amenity": Amenity,
                  "City": City, "Place": Place, "State": State,
                  "Review": Review}

    def all(self):
        """
        Returns the dictionary of objects
        """
        return (self.__objects)

    def new(self, obj):
        """
        Adds the object to the dictionary of objects using the key
        <class name>.<id of the object>
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """
        Serializes the objects to the JSON file defined by __file_path
        """
        ser_dict = {}
        all_dict = FileStorage.__objects
        with open(FileStorage.__file_path, 'w') as f:
            # Convert each object to a dictionary
            for value in all_dict.values():
                key = "{}.{}".format(value.__class__.__name__, value.id)
                ser_dict[key] = value.to_dict()
            # Write the dictionary to the JSON file
            json.dump(ser_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to objects
        Only if the JSON file exists, otherwise does nothing
        """
        # Check if the file exists
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, 'r') as f:
                # Load the JSON data from the file
                des_json = json.load(f)
                for key, value in des_json.items():
                    # Split the key to separate class name and id
                    class_name, obj_id = key.split('.')
                    # Create the object using the class name and data
                    obj = self.class_dict[class_name](**value)
                    # Add the object to the __objects dictionary
                    self.new(obj)
