#!/usr/bin/python3
'''
Python simple module
'''


def append_write(filename="", text=""):
    ''''
    method for writing a file
    '''
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
