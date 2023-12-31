#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Rectangle:
    """
    This is the documentation for the Rectangle class.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Init method for square instances
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2*self.width + 2*self.height

    def __str__(self):
        s = str(self.print_symbol)
        if self.width == 1:
            return s * self.height
        if self.height == 1:
            return s * self.width
        return (s * self.width + '\n') * (self.height - 1) + s * self.width

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
