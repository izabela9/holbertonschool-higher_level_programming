#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


def lookup(obj):
    """
    'print(__import__("my_module").my_function.__doc__)'
    python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
    """
    list = dir(obj)
    return list
