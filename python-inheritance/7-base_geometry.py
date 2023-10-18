#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class BaseGeometry:
    """"
    Class that inherits from list class
    """
    def area(self):
        """"
        Instance method to raise an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """"
         Function for checking an valid integer
         """
        self.__name = name
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.__value = value
