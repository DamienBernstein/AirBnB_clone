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

     def do_create(self, line):
          """
          Create a new instance of BaseModel.
          If class name is missing, prints "** class name missing **".
          If class doesn't exist, prints "** class doesn't exist **".
          """
          # Check if line is empty
          if not line:
              print("** class name missing **")
              return None

          # Check if the class exists
          elif line not in self.level:
              print("** class doesn't exist **")
              return None

          # Create an instance of the class
          else:
              my_inst = eval(line + "()")
              my_inst.save()
              print(my_inst.id)
            
     def do_show(self, line):
          """
          Prints the string representation of an instance based on the class name and id.
          If class name is missing, prints "** class name missing **".
          If class doesn't exist, prints "** class doesn't exist **".
          If instance id is missing, prints "** instance id missing **".
          If instance doesn't exist, prints "** no instance found **".
          """
          # Split the line into a list of commands separated by white space
          n = line.split()

          # Check if line is empty
          if not line:
              print("** class name missing **")
              return None

          # Check if the class exists
          elif n[0] not in self.level:
              print("** class doesn't exist **")
              return None

          # Check if instance id is missing
          elif len(n) == 1:
              print("** instance id missing **")
              return None

          # Search for the instance
          else:
              # Concatenate class_name and id with a dot
              key = "{}.{}".format(n[0], n[1])
              # Search for the key in the storage
              if key not in storage.all().keys():
                  print("** no instance found **")
              else:
                  obj = storage.all()
                  # Print the string representation of the instance with class name and id
                  print(obj[key])
       
            

            

         
     
