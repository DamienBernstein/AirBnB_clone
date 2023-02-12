#!/usr/bin/python3

""" Unittest """


import unittest
import os
from models.user import User
from models.state import State
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    TestAmenity class contains all the test cases for the Amenity class
    """

    @classmethod
    def setUpClass(cls):
        """
        This method creates an instance of the Amenity class for testing
        """
        cls.state1 = State()
        cls.state1.name = "los Durba"

    @classmethod
    def tearDownClass(cls):
        """
        This method deletes the instance of the Amenity class and removes the file created during testing
        """
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict(self):
        """
        This method tests if the to_dict method exists in the Amenity class
        """
        self.assertEqual("to_dict" in dir(self.state1), True)

    def test_functions(self):
        """
        This method tests if the __doc__ string exists for the Amenity class
        """
        self.assertIsNotNone(State.__doc__)

    def test_save(self):
        """
        This method tests if the save method updates the created_at and updated_at attributes correctly
        """
        self.state1.save()
        self.assertNotEqual(self.state1.created_at, self.state1.updated_at)

    def test_subclass(self):
        """
        This method tests if the Amenity class is a subclass of BaseModel
        """
        self.assertTrue(issubclass(self.state1.__class__, BaseModel), True)

    def test_attributes(self):
        """
        This method tests if the Amenity class has all the required attributes
        """
        self.assertTrue("name" in self.state1.__dict__)
        self.assertTrue("created_at" in self.state1.__dict__)
        self.assertTrue("updated_at" in self.state1.__dict__)
        self.assertTrue("id" in self.state1.__dict__)

    def test_strings(self):
        """
        This method tests if the name attribute is a string
        """
        self.assertEqual(type(self.state1.name), str)


if __name__ == "__main__":
    unittest.main()
