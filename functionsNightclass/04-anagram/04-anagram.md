## Anagram function

An anagram is direct word switch or word play, the result of rearranging the letters of a word or phrase to produce a new word or phrase, using all the original letters exactly once. Uppercase and lowercase letters are considered the same and you may add white spaces wherever you want. 

For example, the name "Tom Marvolo Riddle" can be rearranged the sentence "I am Lord Voldemort". Now, given two strings a and b, write a function `is_anagram(a, b)` which returns True if a and b are anagrams of one another, and False otherwise. You may not use any sorting functionality.

You may want to write one or more helper functions to process the input first.

```
# Possibly useful methods (depending on how you implement this) and built-in functions include
# count(list)
# .isalpha
# .lower or .upper
# filter
# .join(stringlist) called with an empty string
# .count(element) method of string or list
```

For example:

```
print(is_anagram("tommarvoloriddle", "iamlordvoldemort")
# prints 'True'

print(is_anagram("carter", "retrace"))
# prints 'False'
```

* Hint: your function can return False as soon as it knows the answer is False

* Challenge: have the function ignore characters that are not letters like it ignores spaces.
