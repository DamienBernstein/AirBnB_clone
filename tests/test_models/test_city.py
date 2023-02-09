#!/usr/bin/python3


"""Unittest User"""


import unittest
import os
from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    """Test class for the City model"""

    @classmethod
    def setUpClass(cls):
        """Setup class method to create an instance of City"""
        cls.city1 = City()
        cls.city1.name = "lalalanda"
        cls.city1.state_id = "tria"

    @classmethod
    def tearDownClass(cls):
        """Teardown class method to delete the instance and remove the file"""
        del cls.city1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict_method(self):
        """Test to check if the to_dict method exists"""
        self.assertIn("to_dict", dir(self.city1))

    def test_docstring(self):
        """Test to check if the class has a docstring"""
        self.assertIsNotNone(City.__doc__)

    def test_save_method(self):
        """Test to check if the save method updates the updated_at attribute"""
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_subclass(self):
        """Test to check if the City class is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attributes(self):
        """Test to check if the city has the expected attributes"""
        self.assertIn("name", self.city1.__dict__)
        self.assertIn("created_at", self.city1.__dict__)
        self.assertIn("updated_at", self.city1.__dict__)
        self.assertIn("id", self.city1.__dict__)
        self.assertIn("state_id", self.city1.__dict__)

    def test_string_attributes(self):
        """Test to check if the name and state_id attributes are strings"""
        self.assertIsInstance(self.city1.name, str)
        self.assertIsInstance(self.city1.state_id, str)

if __name__ == "__main__":
    unittest.main()
