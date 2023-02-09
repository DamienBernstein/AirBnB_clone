#!/usr/bin/python3 


""" Program that contains the entry point of the command interpreter """
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage

class HBNBCommand(cmd.Cmd):
      """ init command prompt """
      prompt = "(hbnb)"
      level = ["BaseModel", "City", "State",
               "User", "Place", "Review", "Amenity"]
      
    # Define a class variable to store all instances of all classes
      all_instances = {}

    # Define a method to retrieve all instances of a class
      @staticmethod
      def retrieve_all(cls):
          """
          Retrieve all instances of a class
          """
          if cls not in HBNBCommand.all_instances:
             HBNBCommand.all_instances[cls] = []
          return [str(instance) for instance in HBNBCommand.all_instances[cls]]

    # Override the default constructor of the cmd.Cmd class
      def __init__(self):
          """
           Initialize the Hbnb class
          """
          super().__init__()


      def do_EOF(self, args):
          """ CTRL-D to exit """
          print()
          return True
      
     
      def do_quit(self, args):
          """ quit the program """
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
                  
      def do_destroy(self, line):
          """
          Deletes an instance based on the class name and id.
          If class name is missing, prints "** class name missing **".
          If class doesn't exist, prints "** class doesn't exist **".
          If instance id is missing, prints "** instance id missing **".
          If instance doesn't exist, prints "** no instance found **".
          """
          n = line.split()

          # Check if class name is missing
          if not line:
              print("** class name missing **")
              return None

          # Check if class exists
          elif n[0] not in self.level:
              print("** class doesn't exist **")
              return None

          # Check if instance id is missing
          elif len(n) == 1:
              print("** instance id missing **")
              return None

          # Delete the instance
          else:
              # Concatenate class_name and id with a dot
              key = "{}.{}".format(n[0], n[1])
              # Search for the key in the storage
              if key not in storage.all().keys():
                  print("** no instance found **")
              else:
                  # Delete the instance
                  del storage.all()[key]
                  # Save the changes in the storage
                  storage.save()


      def do_all(self, line):
          """
          Prints all string representation of all instances based or not on the class name.
          If class doesn't exist, prints "** class doesn't exist **".
          """
          n = line.split()
          obj_list = []

          # Print all instances if class name is not provided
          if len(n) == 0:
              for value in storage.all().values():
                  obj_list.append(value.__str__())
              print(obj_list)

          # Check if class exists
          elif n[0] not in self.level:
              print("** class doesn't exist **")

          # Print all instances of the provided class name
          else:
              for key, value in storage.all().items():
                  if n[0] in key:
                      obj_list.append(storage.all()[key].__str__())
              print(obj_list)

            
      def do_update(self, line):
          """Updates an instance based on the class name and id
          by adding or updating attribute (save the change into the JSON file)
          Usage: update <class name> <id> <attribute name> "<attribute value>"""
          n = line.split()
          if len(n) == 0:
              # Check if the class name is provided
              print("** class name missing **")
          elif (n[0] not in self.level):
              # Check if the class exists
              print("** class doesn't exist **")
          elif len(n) == 1:
              # Check if the instance id is provided
              print("** instance id missing **")
          else:
              obj = storage.all()
              key = "{}.{}".format(n[0], n[1])
              if (key not in obj):
                  # Check if the instance exists
                  print("** no instance found **")
              elif len(n) == 2:
                  # Check if the attribute name is provided
                  print("** attribute name missing **")
              elif len(n) == 3:
                  # Check if the value is provided
                  print("** value missing **")
              else:
                  # Update the attribute value and save the change
                  setattr(obj[key], n[2], n[3])
                  storage.save()

      def do_count(self, line):
          """ retrieve the number of instances of a class """
          count = 0
          # Count the instances of the class
          for key in storage.all().keys():
              if line in key:
                  count += 1
          print(count)

      def default(self, line):
          """ Retrieve instances based on methods, i.e. <class name>.all() """
          n = line.split('.')
          inst = n[0]
          # Check the method and call the appropriate function
          if n[1] == "all()":
              self.do_all(inst)
          elif n[1] == "count()":
              self.do_count(inst)
          elif n[1].startswith('show'):
              idsp = n[1].split('"')
              line = inst + ' ' + idsp[1]
              self.do_show(line)
          elif n[1].startswith('destroy'):
              idsp = n[1].split('"')
              line = inst + ' ' + idsp[1]
              self.do_destroy(line)
          elif n[1].startswith('update'):
              sp = n[1].split('"')
              line = inst + ' ' + sp[1] + ' ' + sp[3] + ' ' + sp[5]
              self.do_update(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    # import sys
    # non-interactive mode
    # if len(sys.argv) > 1:
    # Since onecmd () takes a single string as input
    # the arguments of the program must be joined before passing them
    # HBNBCommand().onecmd(' '.join(sys.argv[1:]))
    # HBNBCommand().cmdloop()
