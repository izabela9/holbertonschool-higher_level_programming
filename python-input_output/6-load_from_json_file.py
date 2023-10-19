#!/usr/bin/python3
'''
Python simple module
'''


import json


def load_from_json_file(filename):
    ''''
    method for writing a function that creates an Object
    from a JSON file
    '''
    with open(filename, "r") as f:
        return json.load(f)
