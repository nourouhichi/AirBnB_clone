#!/usr/bin/python3
"""
New  module
"""


import sys
import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ a command line class """

    prompt = "(hbnb)"

    def emptyline(self):
        """doesn't execute anything when empty line"""
        pass

    def do_EOF(self, line):
        """exits the program by returning True"""
        return True

    def do_quit(self, line):
        """ exits the program when entering the command quit"""
        return True
if __name__ == '__main__':
    HBNBCommand().cmdloop()
