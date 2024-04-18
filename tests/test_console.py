#!/usr/bin/python3
"""
Unit tests for the HBNB console.
"""
import unittest
from unittest.mock import patch
from io import StringIO
import os
import models

from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models.base_model import Base
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """Test cases for the HBNB console."""
    def setUp(self):
        """Set up the test environment."""
        if not os.path.exists("file.json"):
            os.mknod("file.json")
        self.console = HBNBCommand()
        if os.environ.get("HBNB_STORAGE_TYPE") == "db":
            Base.metadata.drop_all(models.storage._DBStorage__engine)
        else:
            models.storage._FileStorage__objects.clear()

    def tearDown(self):
        """Tear down the test environment."""
        if os.path.exists("file.json"):
            os.remove("file.json")
        del self.console

    def test_EOF(self):
        """Test the end-of-file condition."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("EOF")
            self.assertEqual("\n", f.getvalue())  # no output

    def test_quit(self):
        """Test the quit command."""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    def test_help(self):
        """Test the help command."""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
            self.assertIn("Documented commands (type help <topic>):",
                          f.getvalue())

    # Other test methods...
    def test_create(self):
        """Test the create command."""
        # Test with missing class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())

        # Test with non-existent class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Test with BaseModel
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            self.assertEqual(36, len(f.getvalue().strip()))

        # Test with User
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.assertEqual(36, len(f.getvalue().strip()))

        # Test with State
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create State")
            self.assertEqual(36, len(f.getvalue().strip()))

        # Test with City
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create City")
            self.assertEqual(36, len(f.getvalue().strip()))

        # Test with Amenity
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Amenity")
            self.assertEqual(36, len(f.getvalue().strip()))

        # Test with Place
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Place")
            self.assertEqual(36, len(f.getvalue().strip()))

        # Test with Review
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create Review")
            self.assertEqual(36, len(f.getvalue().strip()))

        # Test with specified attributes
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create State name="California" id="tester"')
            self.assertEqual(6, len(f.getvalue().strip()))
            self.console.onecmd("show State tester")
            self.assertEqual('tester', f.getvalue()[0:6])

        # Test with specified attributes for Place
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('create Place city_id="0001" ' +
                                'user_id="0001" name="My_little_house" ' +
                                'number_rooms=4 number_bathrooms=2 ' +
                                'max_guest=10 ' +
                                'price_by_night=300 latitude=37.773972 ' +
                                'longitude=-122.431297')
            uid = f.getvalue().strip()
            self.assertEqual(36, len(uid))
            self.console.onecmd("show Place {}".format(uid))
            self.assertIn('My little house', f.getvalue())

    def test_show(self):
        """Test the show command."""
        # Test with missing class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show")
            self.assertEqual("** class name missing **\n", f.getvalue())

        # Test with non-existent class name
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Test with BaseModel
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Test with User
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show User")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Test with State
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show State")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Test with City
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show City")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Test with Amenity
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Amenity")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Test with Place
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Place")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Test with Review
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show Review")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()
            self.console.onecmd("show BaseModel {}".format(key))
            self.assertIn(key, f.getvalue())


    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all User")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all State")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all City")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Amenity")
            self.assertEqual("[]\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all Place")
            self.assertEqual("[]\n", f.getvalue())


    def test_emptyline(self):
        """Test the emptyline command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("")
            self.assertEqual("", f.getvalue())

    def test_destroy(self):
        """Test the destroy command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy")
            self.assertEqual("** class name missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel")
            self.assertEqual("** instance id missing **\n", f.getvalue())

        # Test destroy command for each model
        models = ["User", "State", "City", "Amenity", "Place", "Review"]
        for model in models:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"destroy {model}")
                self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(key))
            self.assertEqual("", f.getvalue())

    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Test all command for each model
        models = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for model in models:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"all {model}")
                self.assertEqual("[]\n", f.getvalue())

        # Create an instance to test all command
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"all BaseModel")
            self.assertIn(key, f.getvalue())

    def test_update(self):
        """Test the update command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update")
            self.assertEqual("** class name missing **\n", f.getvalue())

        # Test update command for each model
        models = ["MyModel", "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for model in models:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"update {model}")
                self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel 1234-1234-1234")
            self.assertEqual("** no instance found **\n", f.getvalue())

        # Create an instance to test update command
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
            key = f.getvalue().strip()

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update BaseModel {key} name "Betty"')
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {key}")
            self.assertIn("Betty", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f'update BaseModel {key} email "betty@holberton.com"')
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd(f"show BaseModel {key}")
            self.assertIn("betty@holberton.com", f.getvalue())

    def test_count(self):
        """Test the count command."""
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count MyModel")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())

        # Test count command for each model
        models = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
        for model in models:
            with patch('sys.stdout', new=StringIO()) as f:
                self.console.onecmd(f"count {model}")
                self.assertEqual("0\n", f.getvalue())

        # Create instances to test count command
        self.console.onecmd("create User")
        self.console.onecmd("create City")
        self.console.onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("count User")
            self.assertEqual("2\n", f.getvalue())

    def test_all_dot_commands(self):
        """Test the all dot commands."""
        uid = None
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            uid = f.getvalue().strip()

        # Test show dot command
        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.show()")
            self.console.onecmd(processed_line)
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd(f'User.show("{}")'.format(uid))
            self.console.onecmd(processed_line)
            self.assertIn(uid, f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.count()")
            self.console.onecmd(processed_line)
            self.assertEqual("1\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.update()")
            self.console.onecmd(processed_line)
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.update("{}"'.format(uid)
                                                 + ', "name", "Betty")')
            self.console.onecmd(processed_line)
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.show("{}")'.format(uid))
            self.console.onecmd(processed_line)
            self.assertIn("Betty", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.update("' + uid +
                                                 '", { "name": "Holberton", '
                                                 + '"email": "b@hbtn.com" })')
            self.console.onecmd(processed_line)
            self.assertEqual("", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.show("{}")'.format(uid))
            self.console.onecmd(processed_line)
            output = f.getvalue()
            self.assertIn("Holberton", output)
            self.assertIn("b@hbtn.com", output)

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd("User.destroy()")
            self.console.onecmd(processed_line)
            self.assertEqual("** instance id missing **\n", f.getvalue())

        with patch('sys.stdout', new=StringIO()) as f:
            processed_line = self.console.precmd('User.destroy("{}")'
                                                 .format(uid))
            self.console.onecmd(processed_line)
            self.assertEqual("", f.getvalue())
