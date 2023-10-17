#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def is_kind_of_class(obj, a_class):
    """"
    Returns true if object is an instance
    of the specified class or the class that inherited from
    the specified class
    """
    return isinstance(obj, a_class)
