
import json


def open_list():
    with open('lists.json', 'r') as lists_file:
        for lines in lists_file:
            
            print(lines)

open_list()