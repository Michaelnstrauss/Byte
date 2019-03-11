#!/usr/bin/env python3
#problem1
import random

data = []
for i in range(20):
    data.append(random.randint(0,99))

for val in data:
    print(val)

final = data.pop()
print('the final element was', final)

data.insert(3, 0)

print(data[-5:])

sorted_data = sorted(data)

sorted_data.reverse()

print(sorted_data)

print(sorted_data.index(0))

new_list = []
for element in data:
    if element % 2 == 0:
        new_list.append(element // 2)
print(new_list)

print(data.count(0))

print(sum(data))

strlist = []
for element in data:
    strlist.append(str(element))

strlist = [str(element) for element in data]
