#!/usr/bin/python3
""" First User in AirBnB Project """
from .base_model import BaseModel
from models.base_model import BaseModel


class User(BaseModel):
    """ class User that inherits from BaseModel """
    first_name = ''
    Last_name = ''
    email = ''
    password = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
