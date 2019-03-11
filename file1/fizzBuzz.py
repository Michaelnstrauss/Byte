#!/usr/bin/env python3

user_input = int(input('what number would you like to run in the model: '))

def fizzBuzz(user_input):
    for x in range(0,user_input):
        if x % 3 == 0 and x % 5 == 0:
             print('FizzBuzz')
        elif x % 3 == 0:
             print('Fizz')
        elif x % 5 == 0:
            print('Buzz')
        else:
            print(x)

if __name__=='__main__':
    fizzBuzz(user_input)
