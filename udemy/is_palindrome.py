

string1 = 'anna'

'''def is_palindrome(string1):
    str2 = ''
    for letter in string1:
        str2 = letter + str2
    if string1 == str2:
        return True
    return False'''

def is_palindrome(string1):
    return string1 == string1[::-1]

print(is_palindrome(string1))