#!/usr/bin/python3


""" Unittest"""


import unittest
import os
from models.review import Review
from models.base_model import BaseModel

# Test class for Review model
class TestReview(unittest.TestCase):

    # Setup method to initialize a Review object
    @classmethod
    def setUpClass(cls):
        cls.review = Review()
        cls.review.user_id = "tim"
        cls.review.place_id = "lalalanda"
        cls.review.text = "I'll be back"

    # Tear down method to delete the Review object and remove the file if exists
    @classmethod
    def tearDownClass(cls):
        del cls.review
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    # Test the presence of to_dict method
    def test_to_dict(self):
        self.assertEqual("to_dict" in dir(self.review), True)

    # Test if the __doc__ attribute of the Review class is not None
    def test_functions(self):
        self.assertIsNotNone(Review.__doc__)

    # Test the save method of the Review class
    def test_save(self):
        self.review.save()
        self.assertNotEqual(self.review.created_at, self.review.updated_at)

    # Test if the Review class is a subclass of BaseModel
    def test_subclass(self):
        self.assertTrue(issubclass(self.review.__class__, BaseModel), True)

    # Test the presence of necessary attributes in the Review object
    def test_attributes(self):
        self.assertTrue("created_at" in self.review.__dict__)
        self.assertTrue("updated_at" in self.review.__dict__)
        self.assertTrue("user_id" in self.review.__dict__)
        self.assertTrue("place_id" in self.review.__dict__)
        self.assertTrue("text" in self.review.__dict__)
        self.assertTrue("id" in self.review.__dict__)

    # Test if the type of the attributes of the Review object is correct
    def test_strings(self):
        self.assertEqual(type(self.review.text), str)
        self.assertEqual(type(self.review.place_id), str)
        self.assertEqual(type(self.review.user_id), str)

# Main block to run the tests
if __name__ == "__main__":
    unittest.main()
