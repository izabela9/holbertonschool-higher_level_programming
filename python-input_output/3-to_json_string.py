#!/usr/bin/python3
'''
Python simple module
'''


import json


def to_json_string(my_obj):
    ''''
    method for returning the json representation
    of an object
    '''
    return json.dumps(my_obj)
