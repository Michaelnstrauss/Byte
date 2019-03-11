#!/usr/bin/env python3


'''for num in range(1, 21):
    if num % 2 == 0:
        if num == 4:
            print('UNLUCKY!')
        else:
            print(f'{num} is even')
    else:
        if num == 13:
            print('UNLUCKY!')
        else:
            print(f'{num} is odd')'''


for num in range(1, 21):
    if num ==4 or num==13:
        state = 'unlucky'
    elif num % 2 == 0:
        state = 'even'
    else:
        state = 'odd'
    print(f'{num} is {state}')
