#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        new_list = my_list[::-1]
        for int in new_list:
            print("{:d}".format(int))
