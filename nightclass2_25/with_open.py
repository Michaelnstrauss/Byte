#!/usr/bin/env python3


with open('words.txt', 'r') as input_file, open('capswords.txt', 'w') as output_file:
    for line in input_file:
        capsline = line.upper()
        print(capsline, end='', file=output_file)
