

string1 = 'awesome'

def multiple_letter_count(string1):
    return {letter: string1.count(letter) for letter in string1}

print(multiple_letter_count(string1))