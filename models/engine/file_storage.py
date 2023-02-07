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

   

    
       
   
