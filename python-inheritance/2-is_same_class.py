#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def is_same_class(obj, a_class):
    """"
    Returns true if object is exactly an instance
    of the specified class
    """
    if type(obj) is a_class:
        return True
    return False
