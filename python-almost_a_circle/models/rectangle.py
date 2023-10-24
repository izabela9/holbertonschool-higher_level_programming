#!/usr/bin/python3
'''
Module for demostrattive purposes
'''


from models.base import Base


class Rectangle(Base):
    '''
    Class for Rectangle objects
    '''

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        '''
        Function to calculate the area of the rectangle
        '''
        return self.width * self.height

    def display(self):
        '''
        Function to display the rectangle with #
        '''
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle]\
 ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args):
        '''
        update function 
        '''
        for arg in args:
            if len(args) == 1:
                self.id = args[0]
            elif len(args) == 2:
                self.width = args[1]
            elif len(args) == 3:
                self.height = args[2]
            elif len(args) == 4:
                self.x = args[3]
            elif len(args) == 5:
                self.y = args[4]
