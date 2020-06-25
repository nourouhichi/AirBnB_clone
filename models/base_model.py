#!/usr/bin/python3
""" Base Module module"""


import uuid
import datetime


class BaseModel:

    """ define all common attributes"""

    def __init__(self):
        """ instantination"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = None

    def __str__(self):
        """ returns a string object"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute"""

        super().__init__()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """ returns a dictionary containing all key/values of __dict__"""
        super().__init__()
        dict = self.__dict__
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dict.update({'__class__': self.__class__.__name__})
        return dict
