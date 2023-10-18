#!/usr/bin/python3
'''
Python simple module
for demonstarative purpose
'''


def read_file(filename=""):
    ''''
    method for reading a file
    '''
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read())
