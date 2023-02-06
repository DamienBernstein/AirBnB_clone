#!/usr/bin/python3


"""Base Model"""
import uuid
from datetime import datetime
# import the variable storage
import models


class BaseModel:
  """ class for all other classes to inherit from """
   def __init__(self, *args, **kwargs):
        """ Constructor and re-create an instance with
        this dictionary representation"""
        if len(kwargs) > 0:
            # each key of this dictionary is an attribute name
            # each value of this dictionary is the value of this attribute name
            for key, value in kwargs.items():
                if key == "updated_at":
                    # Convert string date to datetime object
                    # strptime (string parse time): Parse a string into a -
                    # datetime object given a corresponding format
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    # This happens because __class__ is not mandatory in output
                    continue

                setattr(self, key, value)
        else:
            # Generate a random UUID
            self.id = str(uuid.uuid4())
            # assign with the current datetime when an instance is created
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # if it’s a new instance add a call to the method new(self) on stge
            models.storage.new(self)
            
     def __str__(self):
        """ overriding the __str__ method that returns a custom
        string object """
        # Old-style: self.__class__.__name__
        class_name = type(self).__name__
        mssg = "[{0}] ({1}) {2}".format(class_name, self.id, self.__dict__)
        return (mssg)
