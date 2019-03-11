

list1 = [1,2,3]

list2 = [2,3,4]

def intersection(list1, list2):
    list3 = []
    for val in list1:
        list_a = val
        if val in list2:
            list3.append(list_a)
    return list3


#    return [list1 for list1 in list2 if list2 in list1]

    


print(intersection(list1,list2))
