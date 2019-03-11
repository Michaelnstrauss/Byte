import os
import random

DIR = os.path.dirname(__file__)
FILENAME = "grid.txt"
PATH = os.path.join(DIR, FILENAME)

with open(PATH, 'w') as file_object:
    for rownum in range(5):
        for colnum in range(10):
            print(random.randint(5, 9), file=file_object, end=' ')
        print(file=file_object)
