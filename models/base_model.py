#!/usr/bin/python3


""" Base module """
import uuid
from datetime import datetime
# import the variable storage
import models


class BaseModel:
    """ 
    Base class for other classes to inherit from 
    """
    def __init__(self, *args, **kwargs):
        # Generate a random UUID for each instance
        self.id = str(uuid.uuid4())
        # Set the created_at time to the current time
        self.created_at = datetime.now()
        # Set the updated_at time to the current time
        self.updated_at = datetime.now()

        # If kwargs is not empty (i.e. there are additional attributes)
        if kwargs:
            # Call the helper function to recreate the instance from the kwargs
            self._recreate_from_dict(kwargs)
            # Add the instance to the storage
            models.storage.new(self)
    
    def _recreate_from_dict(self, data):
        # Iterate through each key-value pair in the data dictionary
        for key, value in data.items():
            # If the key is "updated_at", parse the string into a datetime object
            if key == "updated_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            # If the key is "created_at", parse the string into a datetime object
            elif key == "created_at":
                value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
            # If the key is "__class__", skip it
            elif key == "__class__":
                continue

            # Set the value of the attribute with the given key
            setattr(self, key, value)

  def __str__(self):
    """
    Overriding the built-in `__str__` method to return a custom string representation
    of the object
    """
    # Get the name of the class as a string
    class_name = type(self).__name__
    # Use an f-string to build the string representation
    return f"[{class_name}] ({self.id}) {self.__dict__}"


   def save(self):
    """
    Save the current state of the object to the file
    """
    # Update the `updated_at` attribute with the current datetime
    self.updated_at = datetime.now()
    # Call the save method of the storage object to persist the changes
    models.storage.save()
