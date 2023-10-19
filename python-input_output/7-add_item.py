#!/usr/bin/python3
'''
Python simple module
'''
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
my_list = []

with open(filename, 'a+', encoding="utf-8") as f:
    my_list.extend(args[1:])
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
