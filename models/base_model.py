#!/usr/bin/python3
""" Base module """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class for all other classes to inherit from """
    def __init__(self, *args, **kwargs):
        """ Constructor and re-create an instance with
        this dictionary representation"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "updated_at" or key == "created_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ overriding the __str__ method that returns a custom
        string object """
        class_name = type(self).__name__
        mssg = f"[{class_name}] ({self.id}) {self.__dict__}"
        return mssg

    def save(self):
        """ updates the public instance attribute updated_at with
        the current datetime """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance."""
        tdic = {}
        tdic["__class__"] = type(self).__name__
        for attr, value in self.__dict__.items():
            if isinstance(value, datetime):
                tdic[attr] = value.isoformat()
            else:
                tdic[attr] = value
        return tdic
