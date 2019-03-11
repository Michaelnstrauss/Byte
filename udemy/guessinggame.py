#!/usr/bin/env python3

from random import randint

random_number = randint(1,10)



while guess != random_number:
    guess = input('What is your guess?\n')
    print('try again!')
