#!/usr/bin/python3
'''
Python simple module
'''


def write_file(filename="", text=""):
    ''''
    method for writing a file
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
