#!/usr/bin/python3

"""Unittest BaseModel"""

import unittest
import os
import uuid
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        base_model = BaseModel()
        self.assertIsInstance(base_model, BaseModel)
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)
        
    # in tests/test_models/test_base_model.py
    def test_recreate_from_dict(self):
        # ...
        recreated_base_model = BaseModel(**data)
    
    def test_recreate_from_dict(self):
        base_model = BaseModel()
        data = base_model.to_dict()
        recreated_base_model = BaseModel(**data)
        self.assertEqual(recreated_base_model.to_dict(), data)
        
        
    def test_str(self):
        base_model = BaseModel()
        string_representation = str(base_model)
        self.assertIn(base_model.id, string_representation)
        self.assertIn(type(base_model).__name__, string_representation)
        self.assertIn(str(base_model.__dict__), string_representation)
    
    def test_save(self):
        base_model = BaseModel()
        updated_at_before_save = base_model.updated_at
        base_model.save()
        updated_at_after_save = base_model.updated_at
        self.assertNotEqual(updated_at_before_save, updated_at_after_save)
        
    def test_to_dict(self):
        base_model = BaseModel()
        data = base_model.to_dict()
        self.assertIn("__class__", data)
        self.assertEqual(data["__class__"], type(base_model).__name__)
        self.assertIsInstance(data["created_at"], str)
        self.assertIsInstance(data["updated_at"], str)

if __name__ == '__main__':
    unittest.main()
