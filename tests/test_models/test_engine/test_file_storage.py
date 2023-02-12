#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User
from models.engine.file_storage import FileStorage

# class that tests the file storage class
class TestFileStorage(unittest.TestCase):
    
   
    # setup method to initialize the review object before running tests
    @classmethod
    def setUpClass(cls):
        cls.review = Review()
        cls.review.user_id = "tim"
        cls.review.place_id = "lalanda"
        cls.review.text = "I'll be back"

    # teardown method to delete the review object and remove the file.json file
    # after all tests have run
    @classmethod
    def tearDownClass(cls):
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

        tidus = tidus() # create an instance of the Tidus class
        file_storage = FileStorage()
        file_storage.new(tidus.__class__.__name__, tidus)

    # test the new method of the file storage class
    def test_new_method(self):
        # initialize the file storage object
        file_storage = FileStorage()
        # get the dictionary of instances stored in the file
        instances_dict = file_storage.all()
        # create a user object
        tidus = User()
        tidus.id = 999999
        tidus.name = "tidus"
        # add the user object to the file storage
        file_storage.new(tidus)
        # generate the key that should be used to access the user object in the dictionary of instances
        key = tidus.__class__.__name__ + "." + str(tidus.id)
        # check if the key is present in the dictionary of instances
        self.assertIn(key, instances_dict)

    # test the all method of the file storage class
    def test_all_method(self):
        # initialize the file storage object
        file_storage = FileStorage()
        # get the dictionary of instances stored in the file
        instances_dict = file_storage.all()
        # check if the returned value is a dictionary
        self.assertIsInstance(instances_dict, dict)
        # check if the returned value is equal to the __objects attribute of the file storage object
        self.assertEqual(instances_dict, file_storage._FileStorage__objects)

    # test the reload method of the file storage class
    def test_reload_method(self):
        # initialize the file storage object
        file_storage = FileStorage()
        # try to remove the file.json file
        try:
            os.remove("file.json")
        except:
            pass
        # create an empty file.json file
        with open("file.json", mode="w") as f:
            f.write("{}")
        # check if the reload method returns None
        self.assertIsNone(file_storage.reload())

# if this module is run as the main module, run the tests
if __name__ == "__main__":
    unittest.main()

