#!/usr/bin/python3
""" This module defines the unittests for the Class Amenity. """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test suite for the Amenity class."""

    def test_amenity_instance(self):
        """Test if an Amenity instance is created."""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_amenity_attributes(self):
        """Test if Amenity instance has the expected attributes."""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))

    def test_amenity_name_default_value(self):
        """Test if Amenity name attribute has the default value."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_to_dict(self):
        """Test conversion of Amenity instance to dictionary."""
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_amenity_str_representation(self):
        """Test string representation of Amenity instance."""
        amenity = Amenity()
        amenity_str = str(amenity)
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(amenity_str, expected_str)


if __name__ == "__main__":
    unittest.main()
