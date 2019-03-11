#!/usr/bin/env python3

import statistics
from collections import Counter

variable_array = [2, 34, 12, 29, 38, 1, 12, 8, 8, 9, 29, 38, 8, 9, 2, 3, 7, 10, 12, 8, 34, 7]

def array(variable_array):
    print(statistics.median(variable_array))
    print(statistics.mean(variable_array))
    print(statistics.mode(variable_array))

    #return median number in array
    #return average number in array
    #return most frequent number in array

if __name__ == '__main__':
    array(variable_array)
