#!/usr/bin/python3


""" Base module """
import uuid
from datetime import datetime
# import the variable storage
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        storage = FileStorage()
        storage.new(self)

    def _recreate_from_dict(self, data):
        """Helper function to recreate the instance from a dictionary."""
        for key, value in data.items():
            if key == "updated_at":
                value = datetime.fromisoformat(value)
            elif key == "created_at":
                value = datetime.fromisoformat(value)
            elif key == "__class__":
                continue

            setattr(self, key, value)

    def __str__(self):
        """Return a custom string representation of the object."""
        class_name = type(self).__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current state of the object to the file."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__ of the instance."""
        tdic = {}
        tdic["__class__"] = type(self).__name__
        for n, i in self.__dict__.items():
            if isinstance(i, datetime):
                tdic[n] = i.isoformat()
            else:
                tdic[n] = i
        return tdic
