#!/usr/bin/env python3



def div7(numbers):
    if numbers % 7 == 0:
        return True
    if numbers % 7 != 0:
        return False

print(div7(14))


def islong(_string):
    if len(_string) >= 10:
        return True
    else:
        return False

print(islong('wooooooooooooowww'))

def firstletter(_string):
    for first in _string[0]:
        return first

print(firstletter('wow'))

def zerolist(number):
    zerolist = []
    for num in range(number):
        zerolist.append(None)
    return zerolist

#    for num in range(number):
#        print('None'.split())
#    return zerolist
#    print(zerolist)


#def zerolist(number):
#    return 'None'.split() * number

print(zerolist(4))


def strconvert(alist):
    empty_list = []
    for num in alist:
        empty_list.append(str(num))
    return empty_list


mylist = [1,2,3,4,5]
newlist = strconvert(mylist)
print(newlist)

def printbar(length):
    len(length) = '-'
    for num in range(length):
        return str('+' + (length-2) + '+')

if __name__=='__main__':
    printbar(2)
