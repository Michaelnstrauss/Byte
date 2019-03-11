


# a_list = [1,10,100,1000,10000]
# empty_list = []
# def every_other_element(a_list):
#     for item in range(len(a_list)):
#         if item == 0 or item % 2 == 0:
#             items_list = str(a_list[item])
#             items_list = items_list.split()
#             items_list = empty_list.extend(items_list)
#             #items_list = empty_list.append(items_list)
#             #print(items_list)

#every_other_element(a_list)

a_string = 'look!'

def three_times(a_string):
    return str(a_string) * 3

print(three_times(a_string))

numbers = [1,2,3,4,]

def str_converter(numbers):
    numbers_list = []
    for number in numbers:
        string_number = str(number)
        numbers_list += string_number
    print(numbers_list)

str_converter(numbers)