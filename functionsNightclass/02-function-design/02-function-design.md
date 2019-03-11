## Function Design

#### Write the following functions. Pick descriptive names for the functions and their parameters.

* Remember that print and return serve different purposes. Remember that a function recieves its parameters through the variables in its definition. Most functions will not use print() or input().

#### Questions:

* A function that returns True if a number is divisible by 7 and False if it does not.

```python
def div7(number):
    # your definition

print(div7(14))  # will print 'True'
```

* (A function that returns True if a string is 10 characters or longer and False if it does not.

```python
def islong(string):
    # your definition

print(islong("Shorty"))  # will print 'False'
```

* A function that returns the first letter of a string

```python
def firstletter(string)
    # your definition

print(firstletter("Hello!"))  # will print 'H'```
```

* A function that takes an integer and returns a list with that many elements, where every element is zero.

```python
def zerolist(number):
    # your definition

print(zerolist(4))  # will print [None, None, None, None]
```

* A function that takes a list as its input and returns a new list where each element is the original element converted into a string

```python
def strconvert(alist):
    # yourcode here

mylist = [1,2,3,4,5]
newlist = strconvert(mylist)  # newlist will be ['1', '2', '3', '4', '5']
```

* A function with an integer parameter. It *prints* a string with that length that is dashes between two plus signs. like ```'+---+'``` for 5.

```python
def printbar(length):
    # your code here

printbar(2)  # prints '++'
printbar(5)  # prints '+---+'
printbar(8)  # prints '+------+'
```

* A function that takes two integers, one that represents a width and one that represents a height, and returns a new two dimensional array, where each element is None

```python
def creatematrix(width, height):
    # your code here

matrix = creatematrix(4,3)

# returns [[None, None, None, None], [None, None, None, None], [None, None, None, None]]
```
