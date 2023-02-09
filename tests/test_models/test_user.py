#!/usr/bin/python3

""" Unittest """

import unittest
import os
from models.user import User
from models.base_model import BaseModel

# Test case class for User model
class TestUser(unittest.TestCase):

    # Set up method that runs before each test case
    @classmethod
    def setUpClass(cls):
        cls.my_user = User()
        cls.my_user.first_name = "John"
        cls.my_user.last_name = "Peterstone"
        cls.my_user.email = "josto@jesto.lov"
        cls.my_user.password = "root"

    # Tear down method that runs after each test case
    @classmethod
    def tearDownClass(cls):
        del cls.my_user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    # Test the to_dict method of the User model
    def test_to_dict(self):
        self.assertIn("to_dict", dir(self.my_user))

    # Test the subclass relationship of the User model with BaseModel
    def test_subclass(self):
        self.assertIsNotNone(User.__doc__)
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel))

    # Test the save method of the User model
    def test_save(self):
        self.my_user.save()
        self.assertNotEqual(self.my_user.created_at, self.my_user.updated_at)

    # Test the attributes of the User model
    def test_attributes(self):
        self.assertIn("email", self.my_user.__dict__)
        self.assertIn("password", self.my_user.__dict__)
        self.assertIn("first_name", self.my_user.__dict__)
        self.assertIn("last_name", self.my_user.__dict__)
        self.assertIn("created_at", self.my_user.__dict__)
        self.assertIn("updated_at", self.my_user.__dict__)
        self.assertIn("id", self.my_user.__dict__)

    # Test the types of the attributes of the User model
    def test_strings(self):
        """
        This method tests if the name attribute is a string
        """
        self.assertEqual(type(self.state1.name), str)


# Run the tests if this script is executed as main
if __name__ == "__main__":
    unittest.main()
