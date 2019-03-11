#!/usr/bin/env python3

var1 = int(input('number: '))

def my_loop(var1):
    for var2 in range(var1):
        print(var2)
    for var3 in range(var1,0-1,-1):
        print(var3)

if __name__=='__main__':
    my_loop(var1)
