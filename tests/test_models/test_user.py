#!/usr/bin/python3
""" This module contains unit tests for the User class. """
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test suite for the User class. """

    def tearDown(self):
        """
           Clean up the test environment after each test.
           Remove the test file if it exists.
        """
        if os.path.exists('file.json'):
            os.remove('file.json')

    def test_user_attributes(self):
        """
           Test User instance attributes.
           Verifies that User instances have expected attributes.
        """
        test_user = User()
        self.assertTrue(hasattr(test_user, 'email'))
        self.assertTrue(hasattr(test_user, 'password'))
        self.assertTrue(hasattr(test_user, 'first_name'))
        self.assertTrue(hasattr(test_user, 'last_name'))

    def test_user_instance(self):
        """
           Test User instance creation.
           Verifies that User instances are created as expected.
        """
        test_user = User()
        self.assertIsInstance(test_user, User)
        self.assertIsInstance(test_user, BaseModel)

    def test_user_created_at(self):
        """
           Test User created_at attribute.
           Verifies that User instances have the 'created_at'
           attribute as a datetime.
        """
        test_user = User()
        self.assertTrue(hasattr(test_user, 'created_at'))
        self.assertTrue(isinstance(test_user.created_at, datetime))

    def test_user_updated_at(self):
        """
           Test User updated_at attribute.
           Verifies that User instances have the 'updated_at' attribute
           as a datetime.
        """
        test_user = User()
        self.assertTrue(hasattr(test_user, 'updated_at'))
        self.assertTrue(isinstance(test_user.updated_at, datetime))

    def test_user_save(self):
        """
           Test User save method.
           Verifies that the 'save' method updates the 'updated_at' attribute.
        """
        test_user = User()
        original_updated_at = test_user.updated_at
        test_user.save()
        self.assertNotEqual(original_updated_at, test_user.updated_at)

    def test_user_to_dict(self):
        """
           Test User to_dict method.
           Verifies that the 'to_dict' method returns a dictionary with
           expected keys and values.
        """
        test_user = User()
        user_dict = test_user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], test_user.id)

    def test_user_reload(self):
        """
           Test User reload method.
           Verifies that a User instance is successfully reloaded from storage.
        """
        test_user = User()
        obj_key = "{}.{}".format('User', test_user.id)
        storage.reload()
        self.assertTrue(obj_key in storage.all())


if __name__ == '__main__':
    unittest.main()
