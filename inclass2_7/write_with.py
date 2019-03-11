#!/usr/bin/env python3

with open('outputfile.txt', 'w') as file_object:
    file_object.write('first sting\n')
    file_object.write('second string\n')
    file_object.write('third string\n')


with open('outputfile2.txt', 'w') as file_object:
    file_object.write('first sting\n')
    file_object.write('second string\n')

with open('outputfile3.txt', 'a') as file_object:
    
