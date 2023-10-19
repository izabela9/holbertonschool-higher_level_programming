#!/usr/bin/python3
'''
Python simple module
'''
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv[1:]
filename = "add_item.json"

with open(filename, 'a+', encoding="utf-8") as f:
    my_list = []
    my_list.extend(args)
    save_to_json_file(my_list, filename)
    load_from_json_file(filename)
