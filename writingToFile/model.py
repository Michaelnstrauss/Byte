#!/usr/bin/env python3

import json
import os



def load():
    with open('data.json', 'r') as json_file:
        my_dict = json.load(json_file)
    return my_dict
def save(my_dict):
    with open('data.json', 'w+') as json_file:
        json.dump(my_dict, json_file)
