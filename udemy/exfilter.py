

a_list = [-1,3,4,-99]

def remove_negatives(a_list):
    positive_list = list(filter(lambda num: num > 0, a_list))
    return positive_list



print(remove_negatives(a_list))