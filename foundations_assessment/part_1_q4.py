

user_string = input('Insert input: ')

list_letters = user_string.split()

#print(list_letters)

for letter in user_string.split():
    list_letter = list(letter)
    list_letters = [letter]
    first_letter = list_letters[0] 
    if 'a' or 'e' or 'i' or 'o' or 'u' in first_letter and len(user_string) > 20:
        print('Both tests passed')

    elif 'a' or 'e' or 'i' or 'o' or 'u' in first_letter or len(user_string) > 20:
        print('One of the tests passed')

    else:
        print('Both tests failed')