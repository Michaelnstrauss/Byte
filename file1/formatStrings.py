#!usr/bin/env

x = 3
b = 'little pigs'
print('The {} {}.'.format(x, b))

c = 6.7
print("{:.3f}".format(c))

d = 'Nikil'
e = 'josephine'

print('Look at [{:<15}] now'.format(d))
print("Look at [{:<15}] now".format(e))

print('Look at [{:>15}] now'.format(d))
print("Look at [{:>15}] now".format(e))

print("{:b}".format(13))
