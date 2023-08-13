#!/usr/bin/python3
""" This module contains unit tests for the BaseModel class. """
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ Test suite for the BaseModel class. """

    def test_create_new_instance(self):
        """
            Test creating a new instance of BaseModel.
            Verifies that the instance is of the correct
            class and has the expected attributes.
        """
        obj = BaseModel()
        self.assertIsInstance(obj, BaseModel)
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_custom_id(self):
        """
           Test creating a new instance of BaseModel with a custom ID.
           Verifies that the custom ID is correctly assigned to the instance.
        """
        custom_id = "custom_id"
        obj = BaseModel(id=custom_id)
        self.assertEqual(obj.id, custom_id)

    def test_to_dict(self):
        """
           Test the to_dict method of BaseModel.
           Verifies that the to_dict method returns
           a dictionary with the expected keys and values.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()

        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIsInstance(obj_dict['updated_at'], str)

    def test_from_dict(self):
        """
           Test creating a new BaseModel instance from a dictionary.
           Verifies that the created instance matches the attributes
           from the dictionary.
        """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        new_obj = BaseModel(**obj_dict)

        self.assertIsInstance(new_obj, BaseModel)
        self.assertEqual(new_obj.id, obj.id)
        self.assertEqual(new_obj.created_at, obj.created_at)
        self.assertEqual(new_obj.updated_at, obj.updated_at)

    def test_update_and_save(self):
        """
           Test updating and saving a BaseModel instance.
           Verifies that the 'save' method updates the
           'updated_at' attribute.
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_init_with_kwargs(self):
        """
           Test initializing a BaseModel instance using keyword arguments.
           Verifies that the instance attributes match the provided keyword
           arguments.
        """
        data = {
            'id': '123',
            'created_at': '2023-08-07T15:30:00.000000',
            'updated_at': '2023-08-08T10:45:00.000000',
            'custom_attribute': 'value'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, '123')
        self.assertEqual(obj.custom_attribute, 'value')
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_default_id_generation(self):
        """
           Test the default ID generation of BaseModel.
           Verifies that two instances have different IDs
           when created in succession.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_updated_at_changes(self):
        """
           Test the 'updated_at' attribute changes after
           calling the 'save' method.
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)

    def test_init_with_invalid_datetime_format(self):
        """
           Test initializing a BaseModel instance with an
           invalid datetime format.
           Verifies that a ValueError is raised when the
           datetime format is invalid.
        """
        data = {
            'id': '123',
            'created_at': '2023-08-07 15:30:00',  # Invalid format
            'updated_at': '2023-08-08T10:45:00.000000',
        }
        with self.assertRaises(ValueError):
            obj = BaseModel(**data)

    def test_str_representation(self):
        """
           Test the string representation of BaseModel.
           Verifies that the string representation matches
           the expected format.
        """
        obj = BaseModel()
        string_representation = str(obj)
        expected = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(string_representation, expected)

    def test_instance_equality(self):
        """
        Test equality of two BaseModel instances.
        Verifies that two instances are not equal.
        """
        obj1 = BaseModel()
        obj2 = BaseModel()
        self.assertNotEqual(obj1, obj2)

    def test_custom_attribute_assignment(self):
        """
           Test assigning a custom attribute to BaseModel.
           Verifies that the custom attribute can be assigned
           and accessed.
        """
        obj = BaseModel()
        obj.custom_attr = "test_value"
        self.assertEqual(obj.custom_attr, "test_value")

    def test_attribute_deletion(self):
        """
           Test deleting a custom attribute from BaseModel.
           Verifies that an AttributeError is raised after
           deleting the attribute.
        """
        obj = BaseModel()
        obj.custom_attr = "test_value"
        del obj.custom_attr
        with self.assertRaises(AttributeError):
            value = obj.custom_attr

    def test_updated_at_after_custom_attribute_change(self):
        """
           Test the 'updated_at' attribute changes after modifying and saving.
           Verifies that 'updated_at' changes when a custom attribute is
           modified and saved.
        """
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.custom_attr = "test_value"
        obj.save()
        self.assertNotEqual(old_updated_at, obj.updated_at)


if __name__ == '__main__':
    unittest.main()
