#!/usr/bin/env python3

def reverse_my_string():
    user_input = str(input('enter: '))
    for rev in user_input:
        print(user_input[::-1])
        break
if __name__=='__main__':
    reverse_my_string()
