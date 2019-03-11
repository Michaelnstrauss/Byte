
'''
last_element([1,2,3]) # 3
last_element([]) # None
'''

a_list = [1,2,3,4]

def last_element(a_list):
    return a_list.pop()

print(last_element(a_list))