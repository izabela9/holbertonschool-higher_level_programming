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

    def area(self):
        '''
        Instance method to calculate the area
        of the rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        """
        String represantation of the rectangle
        instance
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
