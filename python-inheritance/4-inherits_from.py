#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""

def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and type(obj) is a_class:
        return False
    return True
