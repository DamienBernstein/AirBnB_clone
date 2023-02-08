#!/usr/bin/python3
""" place of the user """
from . base_model import BaseModel

class Place(BaseModel):
      """ place of user """
      city_id = ' '
      user_id = ' '
      name = ' '
      description = ' ' 
      number_rooms = 0
      number_bedrooms = 0
      max_guests = 0
      price_by_night= 0
      latitude = 0.0
      longitude = 0.0
      amendity_ids = []
