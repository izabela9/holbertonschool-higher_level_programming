#!/usr/bin/python3
'''
Python simple module
'''


import json


def from_json_string(my_str):
    ''''
    method for returning an object
    represented by a JSON string
    '''
    return json.loads(my_str)
