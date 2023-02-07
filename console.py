#!/usr/bin/python3

""" Program that contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place
from models import storage

class HBNBCommand(cmd.Cmd):
      """ init command prompt """
      prompt = "(hbnb)"
      level = ["BaseModel", "City", "State",
               "User", "Place", "Review", "Amenity"]
               
     def do_EDF(self, args):
         """ CTRL-D to exit """
         print()
         return True
         
     def do_quit(self, args):
         """  Quit command to exit the program\n """
         return True
         
     def emptyline(self):
         """ Enter shouldnt execute anything """
         pass
         
     
