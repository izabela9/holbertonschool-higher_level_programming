#!/usr/bin/python3
'''
Python simple module
'''


class Student:
    def __init__(self, first_name, last_name, age):
        '''
        Initialization method for Stduent objects
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Function to returns a dictionary
        represantation of Student object
        '''
        filter_data = {}
        if attrs is None:
            return self.__dict__
        else:
            for attr in attrs:
                if hasattr(self, attr):
                    value = getattr(self, attr)
                    filter_data[attr] = value
            return filter_data

    def reload_from_json(self, json):
        for attr, value in json.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
