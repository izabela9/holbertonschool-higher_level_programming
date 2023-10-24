#!/usr/bin/python3
'''
Module for demostrattive purposes
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Class for square class
    '''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}"

    def update(self, *args, **kwargs):
        '''
        Function to update the instance attributes
        '''
        attributes = ['id', 'size', 'x', 'y']

        for idx in range(len(args)):
            setattr(self, attributes[idx], args[idx])

        if len(args) == 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
