#!/usr/bin/python3
'''
Module for demostrattive purposes
'''


import json


class Base:
    '''
    Class for Base objects
    '''

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        functiont to return dictionry to
        json string
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        function for writing
        the JSON string representation of list_objs to a file
        '''
        if list_objs is not None:
            d_list = [obl.to_dictionary() for obl in list_objs
                  if issubclass(obl.__class__, Base)]
    
        with open(f"{cls.__name__}.json", "w+") as f:
            f.write(cls.to_json_string(d_list))
