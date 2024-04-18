#!/usr/bin/python3
""" Command Line Interface Module """
import cmd
import sys
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    """ Contains functionality for the HBNB console """
    prompt = '(hbnb) '
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']

    def preloop(self):
        """ Handle database initialization """
        pass

    def do_quit(self, _):
        """ Method to exit the HBNB console """
        sys.exit()

    def help_quit(self):
        """ Print help documentation for quit  """
        print("Quit command to exit the program\n\nUsage: quit")

    def do_EOF(self, _):
        """ EOF command to exit the program """
        print()
        return True

    def emptyline(self):
        """ Do nothing when emptyline is entered """
        return False

    def precmd(self, line):
        """
        Called on an input line
        when the command prefix is not recognized
        """
        _cmd = _cls = _id = _args = ''  # Initialize line elements

        # Scan for general formatting - i.e '.', '(', ')'
        if not ('.' in line and '(' in line and ')' in line):
            return line

        pline = line[:]  # Parsed line

        # Isolate <class name>
        _cls = pline[:pline.find('.')]

        # Isolate and validate <command>
        _cmd = pline[pline.find('.') + 1:pline.find('(')]

        # Parse arguments in parenthesis
        pline = pline[pline.find('(') + 1:pline.find(')')]
        if pline:
            # Tokenize args by delimiter (<id>, <args>)
            pline = pline.split(', ', 1)

            # Strip quotes if exist
            _id = pline[0].replace("\"", "")

            # If arguments exist beyond _id
            if len(pline) > 1:
                if "{" in pline[1] and "}" in pline[1] and ":" in pline[1]:
                    idxs = [i for i, ltr in enumerate(pline[1]) if ltr == "\""]
                    if len(idxs) % 2 == 0:
                        return " ".join([_cmd, _cls, _id, pline[1]])
                    new_idxs = [[idxs[i], idxs[i+1]]
                                for i in range(0, len(idxs), 2)]
                    tokens = []
                    for s, e in new_idxs:
                        tokens.append(pline[1][s:e+1])
                    pline[1:] = tokens

                tokens = []
                for token in pline[1:]:
                    tokens.append(token.replace(",", "").replace("\"", ""))
                _args = " ".join(tokens)
        line = ' '.join([_cmd, _cls, _id, _args])
        return line

    def do_create(self, line):
        """ Create an object of any class """
        def parse(s):
            if s.startswith('"') and s.endswith('"'):
                return (s[1:-1].replace("_", " ")
                        if s[1:-1].find(' ') < 0 and
                        (s[1:-1].find('"') < 0
                         or s[s[1:-1].find('"') - 1] == "\\") else None)
            if '.' in s:
                try:
                    s = float(s)
                except ValueError:
                    s = None
            else:
                try:
                    s = int(s)
                except ValueError:
                    s = None
            return s

        if not line:
            print("** class name missing **")
            return
        args = line.split().copy()
        class_name = args[0]
        if class_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        args_dict = {}
        if (len(args) > 1):
            # Parse command syntax to dict
            args_dict = {
                param[0]: parse(param[1])
                for param in (v.split('=') for v in args[1:])
                if parse(param[1])
            }
        new_instance = HBNBCommand.classes[class_name](**args_dict)
        print(new_instance.id)
        new_instance.save()

    def help_create(self):
        """ Help information for the create method """
        print("Creates a class of any type")
        print("[Usage]: create <class_name>\n")

    def do_show(self, line):
        """ Method to show an individual object """
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            print("** instance id missing **")
            return

        c_name = args[0]
        c_id = args[1]
        key = c_name + "." + c_id
        try:
            print(models.storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        """ Help information for the show command """
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        """ Destroys a specified object """
        new = args.partition(" ")
        c_name = new[0]
        c_id = new[2]
        if c_id and ' ' in c_id:
            c_id = c_id.partition(' ')[0]

        if not c_name:
            print("** class name missing **")
            return

        if c_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not c_id:
            print("** instance id missing **")
            return

        key = c_name + "." + c_id

        try:
            del (models.storage.all()[key])
            models.storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        """ Help information for the destroy command """
        print("Destroys an individual instance of a class.\n" +
              "[Usage]: destroy <className> <objectId>")

    def do_all(self, line):
        """ Shows all objects, or all objects of a class """
        if line and line.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            cls = HBNBCommand.classes[line.split()[0]] if line else None
            print([str(v) for v in models.storage.all(cls).values()])

    def help_all(self):
        """ Display help information for the 'all' command """
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        """ Count current number of class instances """
        if not args:
            print("** class name is missing **")
        elif args.split()[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            count = 0
            for key in models.storage.all():
                if args == key.split('.')[0]:
                    count += 1
            print(count)

    def help_count(self):
        """ Display help information for the 'count' command """
        print("Usage: count <class_name>")

    def do_update(self, args):
        """ Updates a certain object with new info """
        class_name = obj_id = attribute = value = ''

        # Isolate class from id/args, ex: (<cls>, delim, <id/args>)
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand.classes:  # class name invalid
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]

        # Generate key from class and id
        key = class_name + "." + obj_id

        # Determine if key is present
        if key not in models.storage.all():
            print("** no instance found **")
            return

        # Retrieve remaining arguments
        new_dict = models.storage.all()[key]
        args = args[2:]
        args = [[args[i], args[i+1]] for i in range(0, len(args), 2)]

        # Iterate through attribute names and values
        for attribute, value in args:
            if not attribute:  # Check for attribute
                print("** attribute name missing **")
                return
            if not value:  # Check for value
                print("** value missing **")
                return

            # Update dictionary with name, value pair
            setattr(new_dict, attribute, value)

        new_dict.save()  # Save updates to file

    def help_update(self):
        """ Display help information for the 'update' command """
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
