#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class that inherits from list class
    '''
    def __init__(self, width, height):
        '''
        Init function for Rectangle class
        '''
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
