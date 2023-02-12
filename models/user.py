#!/usr/bin/python3
""" First User in AirBnB Project """
from .base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel """
    first_name = ''
    Last_name = ''
    email = ''
    password = ''

    # console.py
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

class Console:
    def do_create(self, line):
        if line == "BaseModel":
            new_instance = BaseModel()
        elif line == "User":
            new_instance = User()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, line):
        try:
            class_name, obj_id = line.split()
            obj = storage.
