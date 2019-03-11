
num1 = input('Number 1: ')
num2 = input('Number 2: ')
num3 = input('Number 3: ')

def three_floating(num1, num2, num3):
    add_two = float(num1) + float(num2)
    multi_last = add_two * float(num3)
    print('your floating return is {0:.3f}'.format(multi_last))

three_floating(num1, num2, num3)