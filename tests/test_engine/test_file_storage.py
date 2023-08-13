#!/usr/python3
"""This module defines unit tests for the FileStorage class."""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from datetime import datetime
import os
import json


class TestFileStorage(unittest.TestCase):
    """Test suite for the FileStorage class."""

    def setUp(self):
        """Set up the test environment before each test."""
        self.test_file = 'test_file.json'
        storage._FileStorage__file_path = self.test_file
        self.storage = FileStorage()
        self.base_model_data = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2023-08-07T15:30:00.000000',
            'updated_at': '2023-08-08T10:45:00.000000',
        }

    def test_all(self):
        """Test the 'all' method of FileStorage."""
        obj = BaseModel()
        storage.new(obj)
        objects = storage.all()
        self.assertIn(obj, objects.values())

    def test_new(self):
        """Test the 'new' method of FileStorage."""
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage._FileStorage__objects)

    def test_save(self):
        """Test the 'save' method of FileStorage."""
        storage = FileStorage()
        self.test_file = 'file.json'
        with open(self.test_file, "w") as file:
            file.truncate(0)
        obj = BaseModel()
        storage.new(obj)
        storage.save()
        with open(self.test_file, "r") as file:
            data = file.read()
            self.assertTrue(obj.id in data)

    def test_reload_with_valid_datetime_format(self):
        """Test reloading with valid datetime format in the data."""
        obj_data = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2023-08-07T15:30:00.000000',
            'updated_at': '2023-08-08T10:45:00.000000',
        }
        with open(self.test_file, 'w') as f:
            f.write('{{"{}.{}": {}}}'.format(
                'BaseModel', obj_data['id'], obj_data))

        # Mock the BaseModel class to return a specific instance
        class MockBaseModel:
            def __init__(self, *args, **kwargs):
                pass
        storage._FileStorage__objects = {}
        storage._FileStorage__objects[
            '{}.{}'.format('BaseModel', obj_data['id'])] = MockBaseModel()

        storage.reload()

        key = "{}.{}".format(obj_data['__class__'], obj_data['id'])
        self.assertIn(key, storage._FileStorage__objects)

    def tearDown(self):
        """Clean up the test environment after each test."""
        self.test_file = 'file.json'
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_reload_with_valid_data(self):
        """Test reloading with valid data."""
        # Write a BaseModel data to the test file
        storage = FileStorage()
        self.test_file = 'file.json'
        with open(self.test_file, 'w') as f:
            f.write('{{"{}.{}": {}}}'.format('BaseModel', self.base_model_data[
                'id'], json.dumps(self.base_model_data)))

        # Perform the reload
        storage.reload()

        # Check if the reloaded object matches the original data
        key = "{}.{}".format(self.base_model_data[
            '__class__'], self.base_model_data['id'])
        reloaded_obj = storage._FileStorage__objects.get(key)
        self.assertIsNotNone(reloaded_obj)
        self.assertIsInstance(reloaded_obj, BaseModel)
        self.assertEqual(reloaded_obj.id, self.base_model_data['id'])
        self.assertEqual(reloaded_obj.created_at, datetime.strptime(
            self.base_model_data['created_at'], '%Y-%m-%dT%H:%M:%S.%f'))
        self.assertEqual(reloaded_obj.updated_at, datetime.strptime(
            self.base_model_data['updated_at'], '%Y-%m-%dT%H:%M:%S.%f'))

    def test_reload_with_missing_file(self):
        """Test reloading when the file is missing."""
        # Perform the reload when the file doesn't exist
        self.test_file = 'file.json'
        storage = FileStorage()
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
        storage.reload()

        # Ensure that the __objects dictionary is empty after reloading
        self.assertEqual(storage._FileStorage__objects, {})

    def test_reload_with_invalid_datetime_format(self):
        """Test reloading with invalid datetime format in the data."""
        obj_data = {
            '__class__': 'BaseModel',
            'id': '123',
            'created_at': '2023-08-07T15:30:00.000000',
            'updated_at': '2023-08-08 10:45:00',  # Invalid format
        }
        with open(self.test_file, 'w') as f:
            f.write('{{"{}.{}": {}}}'.format(
                 'BaseModel', obj_data['id'], obj_data))

        storage.reload()
        key = "{}.{}".format(obj_data['__class__'], obj_data['id'])
        self.assertNotIn(key, storage._FileStorage__objects)

    def test_reload_with_invalid_class(self):
        """Test reloading with invalid class reference in the data."""
        obj_data = {
            '__class__': 'NonExistentClass',
            'id': '123',
            'created_at': '2023-08-07T15:30:00.000000',
            'updated_at': '2023-08-08T10:45:00.000000',
        }
        with open(self.test_file, 'w') as f:
            f.write('{{"{}.{}": {}}}'.format(
                'NonExistentClass', obj_data['id'], obj_data))

        storage.reload()
        key = "{}.{}".format(obj_data['__class__'], obj_data['id'])
        self.assertNotIn(key, storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
