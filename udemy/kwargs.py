def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print("{}'s favorite color is {}".format(person,color))


# fav_colors(colt='purple', ruby='red', ethel='teal')
# fav_colors(colt='purple', ruby='red', ethel='teal', ted='blue')
# fav_colors(colt='royal deep purple')

def special_greeting(**kwargs):
    if 'David' in kwargs and kwargs['David'] == 'special':
        return 'You get a special greeting David!'
    elif 'David' in kwargs:
        return "{} David!".format(kwargs['David'])

    return 'Not sure who this is...'

# print(special_greeting(David='Hello'))
# print(special_greeting(Bob='hello'))
# print(special_greeting(David='special'))

# print(special_greeting(Heather='hello', David='special'))

word = 'word'

def combine_words(word,**kwargs):
    if 'prefix' in kwargs:
        return kwargs['prefix'] + word
    if 'suffix' in kwargs:
        return word + kwargs['suffix']
    return word

print(combine_words(word,suffix='ish'))




