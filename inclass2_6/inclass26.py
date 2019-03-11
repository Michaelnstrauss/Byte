#!/usr/bin/env python3

# these two way of generating unsorted_list accomplish
# the exact same thing

from random import randint

unsorted_list = [randint(0,99) for _ in range(30)]

unsorted_list = []
for i in range(30):
    unsorted_list.append(randint(0,99))

def bubble_sort(a_list):
    for i in range(len(a_list)):
        for j in range(len(a_list) - i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]

print(unsorted_list)

bubble_sort(unsorted_list)

print(unsorted_list)
