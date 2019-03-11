#!/usr/bin/env python3

import json
import os

PATH = os.path.dirname(__file__)
DATA = 'data.json'
DATAPATH = os.path.join(PATH, DATA)

data = {}

def load():
    global data
    with open(DATAPATH, 'r') as file_object:
        data = json.load(file_object)
    return data

def save(data):
    with open(DATAPATH, 'w') as file_object:
        json.dump(data, file_object, indent=2)

def add_first_name(f_name):
    return save(f_name)

def add_last_name(l_name):
    return save(l_name)
