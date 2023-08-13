#!/usr/bin/python3
""" This module defines the unittests for the Class City. """
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test suite for the City class."""

    def test_city_instance(self):
        """Test if a City instance is created."""
        city = City()
        self.assertIsInstance(city, City)

    def test_city_attributes(self):
        """Test if City instance has the expected attributes."""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertTrue(hasattr(city, "state_id"))

    def test_city_name_default_value(self):
        """Test if City name attribute has the default value."""
        city = City()
        self.assertEqual(city.name, "")

    def test_city_state_id_default_value(self):
        """Test if City state_id attribute has the default value."""
        city = City()
        self.assertEqual(city.state_id, "")

    def test_city_to_dict(self):
        """Test conversion of City instance to dictionary."""
        city = City()
        city_dict = city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_city_str_representation(self):
        """Test string representation of City instance."""
        city = City()
        city_str = str(city)
        expected_str = "[City] ({}) {}".format(city.id, city.__dict__)
        self.assertEqual(city_str, expected_str)


if __name__ == "__main__":
    unittest.main()
