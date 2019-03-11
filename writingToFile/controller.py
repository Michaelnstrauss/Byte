#!/usr/bin/env python3

import view

import model


def run():
    my_dict = model.load()
    choice(my_dict)
    return my_dict

def choice(my_dict):
    while True:
        key = view.add()
        my_dict[key] = view.value()
        model.save(my_dict)
    return key
#def choice():
#    while True:
#        os.system('clear')
#        view.add()
#        view.value()
#        if view.exit == Y:
#            choice = False
#            model.save()
#    return



if __name__=='__main__':
    run()
