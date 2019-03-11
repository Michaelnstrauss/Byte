#!/usr/bin/env python3

with open('test.txt', 'r') as file_object:
    for line in file_object:
        print(line.split())

print('\n\n\n\n\n')

with open('text.txt', 'r') as file_object:
    line = file_object.readline()
        print(line)
