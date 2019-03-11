
string1 = input('Input string: ')

def length_string(string1):
    len_string1 = len(string1)
    print('The length is {}'.format(len_string1))
    five_into = int(len_string1 / 5)
    five_remainder = len_string1 % 5
    print('5 goes into the length {} times with a remainder of {}'.format(five_into,five_remainder))
    
length_string(string1)