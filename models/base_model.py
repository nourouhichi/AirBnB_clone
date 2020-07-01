#!/usr/bin/python3
""" Base Module module"""


import uuid
import datetime
import models


class BaseModel:

    """ define all common attributes"""

    def __init__(self, *args, **kwargs):
        """ instantination"""

        if kwargs is not {}:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            for k , v in kwargs.items():
                if k is not "__class__":
                    if v is kwargs["created_at"] or v is kwargs["updated_at"]:
                        v = datetime.datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                        setattr(self, k, v)
        else:
            """models.storage.new(self)"""
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            


    def __str__(self):
        """ returns a string object"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ updates the public instance attribute"""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """ returns a dictionary containing all key/values of __dict__"""

        dicta = self.__dict__
        self.created_at = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        self.updated_at = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dicta.update({"__class__": self.__class__.__name__})
        return dicta
