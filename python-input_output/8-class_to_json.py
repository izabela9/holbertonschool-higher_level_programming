#!/usr/bin/python3
'''
Python simple module
'''


import json


def class_to_json(obj):
    '''
    Function to convert an object
    as a json string
    '''
    return obj.__dict__
