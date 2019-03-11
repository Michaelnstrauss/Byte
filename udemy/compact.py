

truthies = [0,1,2,"",[], False, {}, None, "All done"]

def compact(truthies):
    return [val for val in truthies if val]
    
    '''e_list = []
    new_list = [bool(val) for val in truthies]
    return new_list'''
    
    '''for _value in new_list:
    if _value == True:
        print(_value)
            
        e_list += _value
        return e_list


    for _values in truthies:
        print(_values)
        if _values == True:
            val += _values
    return _values'''

print(compact(truthies))
