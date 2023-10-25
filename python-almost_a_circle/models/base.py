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

    def to_json_string(list_dictionaries):
        '''
        functiont to return dictionry to
        json string
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0: 
            return "[]"
        return json.dumps(list_dictionaries)
