#!/usr/bin/env python3

def welcome():
    print('welcome to Terminal Teller!:\n')
    print('1) create account\n')
    print('2) log in\n')
    print('3) quit\n')

def user_choice():
    return int(input('Your choice (enter number please): '))

def first_name_prompt():
    first_name = input("firstname: ")
    return first_name

def last_name_prompt():
    last_name = input('lastname: ')
    return last_name

#def account_creation():
#    print('Account creation\n')
#    first_name = input('First Name: ')
#    last_name = input('Last Name: ')
#    pin = int(input('PIN: '))
#    confirm_pin = int(input('Confirm PIN: '))

#def login():
#    first_name = input('First Name: ')
#    last_name = input('Last Name: ')
#    pin = int(input('PIN: '))

if __name__=='__main__':
    welcome()
    user_choice()
    first_name_prompt()
    last_name_prompt()
