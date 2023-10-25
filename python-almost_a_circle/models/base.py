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
        if list_objs is None:
            list_objs = []

        d_list = [obl.to_dictionary() for obl in list_objs]
        json_string = cls.to_json_string(d_list)

        with open(f"{cls.__name__}.json", "w+") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        '''
        function to return the list of the json string representation
        '''
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Function that creates an instance
        from dictionary given
        '''
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy_instance = cls(1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        '''
        Function that returns a list of instances
        '''
        if os.path.isfile(f"{cls.__name__}.json"):
            with open(f"{cls.__name__}.json") as text_json:
                obj_dict = cls.from_json_string(text_json.read())
                obj_list = []
                for dictionaries in obj_dict:
                    new_obj = cls.create(**dictionaries)
                    obj_list.append(new_obj)
                return obj_list
        else:
            return []
