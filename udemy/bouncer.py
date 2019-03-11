#!/usr/bin/env python3

age = input('What is your age?')

if age:
    age = int(age)
    if age >= 18 and age <= 20:
        print('here is your wrist band')
    elif age < 18:
        print('You are too young and cannot enter')
    else:
        print ('You are over 21')
else:
    print('Please enter age')
