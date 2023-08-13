#!/usr/bin/python3
""" This module contains unittests for the HBNB console. """

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """ Test class for the HBNB console. """

    def tearDown(self):
        """
           Clean up the test environment after each test.
           Remove the test file if it exists.
        """
        self.console = None

    def test_help_quit(self):
        """ Test the help command for quit. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue().strip()
            self.assertIn("Exit the program", output)

    def test_help_EOF(self):
        """ Test the help command for EOF. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue().strip()
            self.assertIn("Exit the program", output)

    def test_create_missing_class(self):
        """ Test the create command with missing class name. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_all_invalid_class(self):
        """ Test the all command with invalid class. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all InvalidClass")
            output = f.getvalue().strip()
            self.assertIn("** class doesn't exist **", output)

    def test_destroy_missing_id(self):
        """ Test the destroy command with missing instance id. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy BaseModel")
            output = f.getvalue().strip()
            self.assertIn("** instance id missing **", output)

    def test_show_missing_class(self):
        """ Test the show command with missing class name. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_update_missing_class(self):
        """ Test the update command with missing class name. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)

    def test_count_missing_class(self):
        """ Test the count command with missing class name. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("count")
            output = f.getvalue().strip()
            self.assertIn("** class name missing **", output)


if __name__ == '__main__':
    unittest.main()
