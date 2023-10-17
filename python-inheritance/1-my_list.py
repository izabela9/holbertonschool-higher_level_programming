#!/usr/bin/python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
"""


class MyList(list):
    """"
    python3 -c 'print(__import__("my_module").MyClass.__doc__)
    """
    def __init__(self):
        """
        'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return super().__init__()

    def print_sorted(self):
        """
        'print(__import__("my_module").my_function.__doc__)'
        python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
        """
        return super().sort()
