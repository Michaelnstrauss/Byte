

a_list = [2,3,4,5,6]


def multiply_even_numbers(a_list):
    total = 1
    for num in a_list:
        if num % 2 == 0:
            total = total * num
    return total

print(multiply_even_numbers(a_list))