#!/usr/bin/python3

""" Unittest """


import unittest
import os
from models.user import User
from models.base_model import BaseModel

# Test class for State Model
class TestState(unittest.TestCase):
    
    # Setup method for class level fixtures
    @classmethod
    def setUpClass(cls):
        cls.state1 = State()
        cls.state1.name = "los Durba"

    # Tear down method for class level fixtures
    @classmethod
    def tearDownClass(cls):
        del cls.state1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    # Test to_dict method of the State model
    def test_to_dict(self):
        self.assertEqual("to_dict" in dir(self.state1), True)

    # Test if State model has docstring
    def test_functions(self):
        self.assertIsNotNone(State.__doc__)

    # Test if save method works as expected
    def test_save(self):
        self.state1.save()
        self.assertNotEqual(self.state1.created_at,
                            self.state1.updated_at)

    # Test if State is a subclass of BaseModel
    def test_subclass(self):
        self.assertTrue(issubclass(self.state1.__class__, BaseModel))

    # Test if State has expected attributes
    def test_attributes(self):
        self.assertTrue("name" in self.state1.__dict__)
        self.assertTrue("created_at" in self.state1.__dict__)
        self.assertTrue("updated_at" in self.state1.__dict__)
        self.assertTrue("id" in self.state1.__dict__)

    # Test if name attribute of the State is a string
    def test_strings(self):
        self.assertEqual(type(self.state1.name), str)

if __name__ == "__main__":
    unittest.main()
