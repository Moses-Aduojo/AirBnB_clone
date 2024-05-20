"""
this module provides functionalities to serializes object instances
to json and as well to deserializes json file to object instances
"""


import json
import os

class FileStorage:
    """
    FileStorage: that serializes instances to a JSON file and deserializes
    JSON file to instances
    attributes:
        __file_path: string - path to the JSON file
        __objects: dictionary - empty but will store all objects by
         <class name>.id
    methods:
        all(self): returns the dictionary __objects
        new(self, obj): sets in __objects the obj with key <obj class name>.id
        save(self): serializes __objects to the JSON file (path: __file_path)
        reload(self): deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist,
        no exception should be raised)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        with open(self.__file_path, 'w') as f:
            json.dump(self.__objects, f)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                try:
                    self.__objects = json.load(f)
                except json.JSONDecodeError:
                    self.__objects = {}
        else:
            self.__objects = {}
