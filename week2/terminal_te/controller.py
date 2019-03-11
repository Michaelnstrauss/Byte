#!/usr/bin/env python3

import model

import view

def run():
    my_dict = model.load()
    user(my_dict)
    return my_dict

def user(my_dict):
    while True:
        print(my_dict)
        view.welcome()
        user_input = view.user_choice()
        print(user_input)
#        if user_input == 3:
#            model.save(data)
#            return
        if user_input == 1:
            key = 'first name'
            f_name = view.first_name_prompt()
            my_dict[key] = f_name
            l_name = view.last_name_prompt()
#            new_account = view.account_creation(user_info)
            model.add_first_name(my_dict)
            model.add_last_name(my_dict)
#            model.add_pin()
#            model.add_confirm_pin()
        elif user_input == 2:
            view.login()

def account():
    pass


if __name__=='__main__':
    run()
