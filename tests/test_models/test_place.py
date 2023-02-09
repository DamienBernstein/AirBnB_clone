# Unittest for User model

import unittest
import os
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    """Test case for the User model"""

    @classmethod
    def setUpClass(cls):
        """Setup method to create an instance of User"""
        cls.user = User()
        cls.user.email = "user1@example.com"
        cls.user.password = "password123"
        cls.user.first_name = "User"
        cls.user.last_name = "One"

    @classmethod
    def tearDownClass(cls):
        """Teardown method to delete the instance of User and the JSON file"""
        del cls.user
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_to_dict_method(self):
        """Test the to_dict method for the User model"""
        self.assertIn("to_dict", dir(self.user))

    def test_docstring(self):
        """Test the docstring for the User model"""
        self.assertIsNotNone(User.__doc__)

    def test_save_method(self):
        """Test the save method for the User model"""
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

    def test_base_model_subclass(self):
        """Test if the User model is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.user.__class__, BaseModel))

    def test_attributes(self):
        """Test the attributes for the User model"""
        self.assertIn("email", self.user.__dict__)
        self.assertIn("password", self.user.__dict__)
        self.assertIn("first_name", self.user.__dict__)
        self.assertIn("last_name", self.user.__dict__)
        self.assertIn("created_at", self.user.__dict__)
        self.assertIn("updated_at", self.user.__dict__)
        self.assertIn("id", self.user.__dict__)

    def test_attribute_types(self):
        """Test the attribute types for the User model"""
        self.assertEqual(type(self.user.email), str)
        self.assertEqual(type(self.user.password), str)
        self.assertEqual(type(self.user.first_name), str)
        self.assertEqual(type(self.user.last_name), str)

if __name__ == "__main__":
    unittest.main()
