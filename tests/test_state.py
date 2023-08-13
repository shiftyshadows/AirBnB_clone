#!/usr/bin/python3
"""This module defines the unit tests for the State class."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ Test suite for the State class. """

    def test_state_instance(self):
        """Test if an instance of the State class can be created."""
        state = State()
        self.assertIsInstance(state, State)

    def test_state_attributes(self):
        """Test if the State instance has the required attributes."""
        state = State()
        self.assertTrue(hasattr(state, "name"))

    def test_state_name_default_value(self):
        """
           Test if the default value of the name attribute
           is an empty string.
        """
        state = State()
        self.assertEqual(state.name, "")

    def test_state_to_dict(self):
        """Test if the to_dict method returns a valid dictionary."""
        state = State()
        state_dict = state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")

    def test_state_str_representation(self):
        """
           Test if the string representation of State matches
           the expected format.
        """
        state = State()
        state_str = str(state)
        expected_str = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(state_str, expected_str)


if __name__ == "__main__":
    unittest.main()
