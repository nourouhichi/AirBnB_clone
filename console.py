#!/usr/bin/python3
"""
"""


import sys
import cmd
import models
from models.base_model import BaseModel
class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    __allclasses= ["BaseModel", "FileStorage"]


    def emptyline(self):
        """doesn't execute anything when empty line"""
        pass
    
    def do_EOF(self, line):
        """exits the program by returning True"""
        return True

    def do_quit(self, line):
        """ exits the program when entering the command quit"""
        quit()

    """def do_create(self):
        """ creates a new instance from an existant class"""
        if sys.argv[1] is None:
            print("** class name missing **")
        elif sys.argv[1] not in HBNBCommand.__allclasses:
            print("** class doesn't exist **")
        else:
            new_inst = eval(sys.argv[1])()
            new_inst.save()
            print(new_inst.id)
    
    def do_show(self):
        """ prints the str representation of an existant object from an existant class"""
        if sys.argv[1] is None:
            print("** class name missing **")
        elif sys.argv[1] not in HBNBCommand.__allclasses:
            print("** class doesn't exist **")
        elif sys.argv[2] is None:
            print("** instance id missing **")
        for k, v in models.storage.all().items:
            if v.id is sys.argv[2] and v.__class__.__name__ is sys.argv[1]:
                print(v)
                return
        print("** no instance found **")

    def do_destroy(self):
        """deletes an existant instance from an existant class """
        if sys.argv[1] is None:
            print("** class name missing **")
        elif sys.argv[1] not in HBNBCommand.__allclasses:
            print("** class doesn't exist **")
        elif sys.argv[2] is None:
            print("** instance id missing **")
        for k, v in models.storage.all().items:
            if v.id is sys.argv[2] and v.__class__.__name__ is sys.argv[1]:
                del(models.storage.all()[k])
                models.storage.save()
                return
        print("** no instance found **")

    def do_all(self):
        """ """"""
        


        

    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()