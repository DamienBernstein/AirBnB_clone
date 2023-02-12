#!/usr/bin/python3


"""Unittest User"""

import unittest
import os
from models.amenity import Amenity
from models.base_model import BaseModel


# class to test the Amenity class
class TestAmenity(unittest.TestCase):

    # method to set up the class before each test method
    @classmethod
    def setUpClass(cls):
        cls.amenity1 = Amenity()
        cls.amenity1.name = "Yggdrasil"

    # method to tear down the class after each test method
    @classmethod
    def tearDownClass(cls):
        del cls.amenity1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    # test method to check if the to_dict method exists
    def test_to_dict(self):
        self.assertTrue(
            "to_dict" in dir(
                self.amenity1),
            "to_dict method not found")

    # test method to check if the class has a __doc__ string
    def test_functions(self):
        self.assertIsNotNone(Amenity.__doc__, "__doc__ string not found")

    # test method to check if the save method updates the created_at and
    # updated_at attributes
    def test_save(self):
        self.amenity1.save()
        self.assertNotEqual(self.amenity1.created_at, self.amenity1.updated_at,
                            "created_at and updated_at are not different")

    # test method to check if the Amenity class is a subclass of BaseModel
    def test_subclass(self):
        self.assertTrue(issubclass(self.amenity1.__class__, BaseModel),
                        "Amenity is not a subclass of BaseModel")

    # test method to check if the required attributes exist in the Amenity
    # class
    def test_attributes(self):
        self.assertIn(
            "name",
            self.amenity1.__dict__,
            "name attribute not found")
        self.assertIn(
            "created_at",
            self.amenity1.__dict__,
            "created_at attribute not found")
        self.assertIn(
            "updated_at",
            self.amenity1.__dict__,
            "updated_at attribute not found")
        self.assertIn("id", self.amenity1.__dict__, "id attribute not found")

    # test method to check if the name attribute is a string
    def test_strings(self):
        self.assertEqual(type(self.amenity1.name), str, "name is not a string")


# run the tests if the module is executed as the main module
if __name__ == "__main__":
    unittest.main()
