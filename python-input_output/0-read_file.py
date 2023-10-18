#!/usr/bin/python3
'''
Python simple module
for demonstarative purpose
'''


def read_file(filename=""):
    ''''
    method for reading a file
    '''
    with open(filename, encoding="utf-8") as f:
        read_file = f.read()
        print(read_file)
