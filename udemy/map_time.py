

a_list = [1,2,3]

# def decrement_list(a_list):
#     for num in a_list:
#         new_list = num-1
#     return new_list


def decrement_list(a_list):
    new_list = list(map(lambda x: x-1, a_list))
    return new_list

print(decrement_list(a_list))