#!/usr/bin/env python3

value = int(input('Give me a number: '))

if value > 100:
    print("That's a big number")
    if value % 2 == 0:
        print('Also it is even')
    else:
        print('Also it is odd')
elif value > 10:
    print("That's not too small")
else:
    print("That's a small number")
