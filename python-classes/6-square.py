#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
"""


class Square:
    """
    This is the documentation for the Square class.
    The class represents a geometric square and associated operations.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) is False or len(value) != 2
            or isinstance(value[0], int) is False or value < 0
                or isinstance(value[1], int) is False or value < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        python3 -c 'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            for c in range(self.__position[0]):
                print(" ", end="")
            for b in range(self.__size):
                print("#", end="")
            print("")
