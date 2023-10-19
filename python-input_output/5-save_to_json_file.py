#!/usr/bin/python3
'''
Python simple module
'''


import json


def save_to_json_file(my_obj, filename):
    ''''
    method for writing an object to a text file
    using a json representation
    '''
    with open(filename, "w", encoding="utf-8") as outfile:
        return json.dump(my_obj, outfile)
