#!/usr/bin/python3
"""
 



"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """ """
    __file_path = "file.json"
    __objects = {}
    allclasses = {"BaseModel": BaseModel}

    def all(self):
        """returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets in some information about the dictionary __objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ loads __objects dictionary to jason format"""
        dictaa = {}
        with open(self.__file_path, mode="w") as f:
            for i, j in self.__objects.items():
                dictaa[i] = j.to_dict()
            json.dump(dictaa, f, indent=4)

    def reload(self):
        """loads the jason format of a dictionary to __object format"""
        name = {}
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r") as f:
                data = json.load(f)
                for k, v in data.items():
                    name[k] = self.allclasses[v["__class__"]](**v)
                self.__objects = name
        else:
            return