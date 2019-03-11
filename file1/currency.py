#!/usr/bin/env python3

#currency types

penny = 1
nickel = 5
dime = 10
quarter = 25
one_dollar = 100
five_dollar = 500
ten_dollar = 1000
fifty_dollar = 5000
hundred_dollar = 10000

def currency_converter():
    amount = float(input('What would you like change for? '))
    change = amount*100
    if change >= hundred_dollar:
        new_change = change / hundred_dollar
        for num_currency in range(int(new_change)):
            print('$100')
        remaining_100  = change % hundred_dollar
        if remaining_100 >= fifty_dollar:
            new_remaining = remaining_100 / fifty_dollar
        for num_currency_50 in range(int(new_remaining)):
            print('$50')
            remaining_50 = remaining_100 % fifty_dollar
            print(remaining_50)
        if remaining_50 >= ten_dollar:
            new_remaining_1 = remaining_50 / ten_dollar:
            print('$10')
#new_change2 = print('$100') for
#        if change >= hundred_dollar:
#        new_change = change % hundred_dollar
#        print('$100')
#        if new_change >
#    elif change >= fifty_dollar:
#        
#     elif change >= ten_dollar:
#        
#    elif change >= five_dollar:
#        
#    elif change >= one_dollar:
#        
#    elif change >= quarter:
#        
#    elif change >= nickel:
#        
#    else change >= penny:
#    return'''

if __name__=='__main__':
    currency_converter()
