#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Rectangle:
    """
    This is the documentation for the Rectangle class.
    """
    def __init__(self, width=0, height=0):
        """
        Init method for square instances
        """
        self.__width = width
        self.__height = height

    '''

    Property getter for attribute width
    '''
    @property
    def width(self):
        return self.__width
    '''

    Property for setting width attribute
    '''
    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    '''

    Property setter for attribute height
    '''
    @property
    def height(self):
        return self.__height
    '''

    Property for setting width attribute
    '''
    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
