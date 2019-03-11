def square(num): return num * num

square2 = lambda num: num * num


add = lambda a,b: a + b

print(square.__name__)
print(square2.__name__)
print(add.__name__)

add_values = lambda x, y: x + y
multiply_values = lambda x, y: x + y
print(add_values(10,20))
print(multiply_values(10,20))