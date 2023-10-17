#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def inherits_from(obj, a_class):
    """"
    Returns true if object is an instance
    of the class that inherited from
    the specified class
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
