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
        self.__height = height
        self.__width = width

    @property
    def width(self):
        '''

        Property getter for attribute width
        '''
        return self.__width

    @width.setter
    def width(self, value):
        '''

        Property for setting width attribute
        '''
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''

        Property setter for attribute height
        '''
        return self.__height

    @height.setter
    def height(self, value):
        '''

        Property for setting width attribute
        '''
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
