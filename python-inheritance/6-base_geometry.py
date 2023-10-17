#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:
    """"
    python3 -c 'print(__import__("my_module").MyClass.__doc__)
    """
    def area(self):
        """"
        Returns the area
        """
        raise Exception("area() is not implemented")
