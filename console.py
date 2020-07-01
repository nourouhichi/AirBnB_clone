#!/usr/bin/python3
"""
New  module
"""

import weakref
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ a command line class """

    prompt = "(hbnb)"
    __allclasses = {"BaseModel": "BaseModel"}

    def emptyline(self):
        """doesn't execute anything when empty line"""
        pass

    def do_EOF(self, line):
        """exits the program by returning True"""
        print()
        return True

    def do_quit(self, line):
        """ exits the program when entering the command quit"""
        return True

    def do_create(self, argv):
        """ creates a new instance from an existant class"""
        argv = argv.split()
        if not argv:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__allclasses:
            print("** class doesn't exist **")
        else:
            new_inst = eval(argv[0])()
            new_inst.save()
            print(new_inst.id)

    def do_show(self, argv):
        """ prints the str representation of an existant object from an existant class"""
        argv = argv.split()
        if not argv:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__allclasses:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            storage.reload()
            for k, v in storage.all().items():
                if v.id == argv[1] and v.__class__.__name__ == argv[0]:
                    print(v.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, argv):
        """deletes an existant instance from an existant class """
        argv = argv.split()
        if not argv:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__allclasses:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        else:
            for k, v in storage.all().items():
                if v.id == argv[1] and v.__class__.__name__ == argv[0]:
                    del(storage.all()[k])
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, argv):
        """ dispalying string repre of all instances """
        check = 0
        argv = argv.split()
        if len(argv) == 0:
            storage.reload()
            inst_list = []
            for k, v in storage.all().items():
                inst_list.append(v.__str__())
            print(inst_list)
        elif len(argv) == 1:
            storage.reload()
            inst_list = []
            for k, v in storage.all().items():
                if v.__class__.__name__ == argv[0]:
                    inst_list.append(v.__str__())
                    check = 1
            if check == 1:
                print(inst_list)
            else:
                print("** class doesn't exist **")
        else:
            pass

    def do_update(self, argv):
        """ updating an object"""
        check = 0
        argv = argv.split()
        if not argv:
            print("** class name missing **")
        elif argv[0] not in HBNBCommand.__allclasses:
            print("** class doesn't exist **")
        elif len(argv) < 2:
            print("** instance id missing **")
        elif argv[1] is not None:
            storage.reload()
            for k, v in storage.all().items():
                if v.id == argv[1]:
                    check = 1
            if check == 0:
                print("** no instance found **")
                return
            elif len(argv) == 2:
                print("** attribute name missing **")
                return
            elif len(argv) == 3:
                print("** value missing **")
                return
            else:
                new = argv[3]
                if hasattr(v, str(argv[2])):
                    new = type(getattr(v, argv[2]))(argv[3])
                v.__dict__[argv[2]] = new
                storage.save()
                return

    def default(self, line):
        counter = 0
        line = line.split('.')
        if line[1] == "count()":
            print(len(storage.all()))

if __name__ == '__main__':
    HBNBCommand().cmdloop()
