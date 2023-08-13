#!/usr/bin/python3
""" This module defines the unittests for the Class Review. """
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test suite for the Review class."""

    def test_review_instance(self):
        """Test if a Review instance is created."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_review_attributes(self):
        """Test if Review instance has the expected attributes."""
        review = Review()
        self.assertTrue(hasattr(review, "place_id"))
        self.assertTrue(hasattr(review, "user_id"))
        self.assertTrue(hasattr(review, "text"))

    def test_review_attributes_default_values(self):
        """Test if Review attributes have the default values."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_to_dict(self):
        """Test conversion of Review instance to dictionary."""
        review = Review()
        review_dict = review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertIn("__class__", review_dict)
        self.assertEqual(review_dict["__class__"], "Review")

    def test_review_str_representation(self):
        """Test string representation of Review instance."""
        review = Review()
        review_str = str(review)
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(review_str, expected_str)


if __name__ == "__main__":
    unittest.main()
