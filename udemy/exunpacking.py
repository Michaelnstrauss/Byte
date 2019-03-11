

def display_names(first, second):
    print('{} says hello to {}'.format(first, second))

names = {'first': 'Colt', 'second': 'Rusty'}

#display_names(**names)

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print('OTHER STUFF...')
    print(kwargs)

data = dict(a=1,b=2,c=3, d=55, name='Tony')

#add_and_multiply_numbers(**data, cat='Blue') 


def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second',0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 0),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)

}
    print(operation_lookup)
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message', 'The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message', 'The result is'), int(operation_value))
    return final

print(calculate(make_float = True, operation = 'add', message='You just added', first=1, second=2))
