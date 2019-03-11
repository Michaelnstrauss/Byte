

def number_compare(num1, num2):
    if num1 > num2:
        return 'First is greater'
    if num2 > num1:
        return 'Second is greater'
    if num1 == num2:
        return 'Numbers are equal'
    else:
        return None
    
print(number_compare(4,4))