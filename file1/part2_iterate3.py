#!/usr/bin/env python3

my_list = [1, 2, ['jeff', 'tom'], [42, ['billy', 'jason']]]

def loop_list():
    print(my_list[0])
    print(my_list[1])
    jeff_tom = my_list[2]
    jeff_tom2 = '\n'.join(jeff_tom)
    print(jeff_tom2)
    forty = my_list[3][0]
    print(forty)
    b_j = my_list[3][1]
    b_j_2 = '\n'.join(b_j)
    print(b_j_2)
   # b_j_42_2 = '/n'.join(str(e) for e in b_j_42)
   # print(b_j_42_2)
#print each out each item in the list

def loop_list_2():
    for x in my_list:
        if type(x) == int:
            print(x)
        elif type(x) == list:
            try:
               print( '\n'.join(x))
            except TypeError:
                print('last line')
     

if __name__=='__main__':
    loop_list_2()
