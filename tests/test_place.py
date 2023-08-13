#!/usr/bin/python3
""" This module defines the unittests for the Class Place. """
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test suite for the Place class."""

    def test_place_instance(self):
        """Test if a Place instance is created."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_place_attributes(self):
        """Test if Place instance has the expected attributes."""
        place = Place()
        self.assertTrue(hasattr(place, "city_id"))
        self.assertTrue(hasattr(place, "user_id"))
        self.assertTrue(hasattr(place, "name"))
        self.assertTrue(hasattr(place, "description"))
        self.assertTrue(hasattr(place, "number_rooms"))
        self.assertTrue(hasattr(place, "number_bathrooms"))
        self.assertTrue(hasattr(place, "max_guest"))
        self.assertTrue(hasattr(place, "price_by_night"))
        self.assertTrue(hasattr(place, "latitude"))
        self.assertTrue(hasattr(place, "longitude"))
        self.assertTrue(hasattr(place, "amenity_ids"))

    def test_place_attributes_default_values(self):
        """Test if Place attributes have the default values."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_to_dict(self):
        """Test conversion of Place instance to dictionary."""
        place = Place()
        place_dict = place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertIn("__class__", place_dict)
        self.assertEqual(place_dict["__class__"], "Place")

    def test_place_str_representation(self):
        """Test string representation of Place instance."""
        place = Place()
        place_str = str(place)
        expected_str = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(place_str, expected_str)


if __name__ == "__main__":
    unittest.main()
