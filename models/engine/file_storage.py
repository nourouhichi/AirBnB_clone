#!/usr/bin/python3
"""
 



"""
import json
from models.base_model import BaseModel
class FileStorage:
    """ """
    __file_path = "file.json"
    __objects = {}
    """allclasses = {"BaseModel": BaseModel}"""

    def all(self):
        """returns a dictionary"""
        return self.__objects

    def new(self, obj):
        """ sets in some information about the dictionary __objects"""
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ loads __objects dictionary to jason format"""
        dictaa = {}
        with open(self.__file_path, mode="w+") as f:
            for i, j in self.__objects.items():
                dictaa[i] = j.to_dict()
            json.dump(dictaa, f)

    def reload(self):
        """loads the jason format of a dictionary to __object format"""
        name = {}
        try:
            with open(self.__file_path, mode="r+") as f:
                data = json.load(f)
                # for v in list(data.values()):
                #     name = 
            for v in data.values():
                classes = v["__class__"]
                classes = eval(classes)
                self.new(classes(**v))
        except FileNotFoundError:
            pass
        
        