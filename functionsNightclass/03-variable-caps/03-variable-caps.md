## Variable Caps

* Write a function that takes a string as its argument

* If the word is 4 characters or shorter, return the argument in UPPERCASE. If the word is 4 letters or longer, return the word in lowercase.

```python
process_word("The")  # returns 'THE'

process_word("Answer") # returns 'answer'

# hint .upper(), .lower()

```
* Write a second function that takes a string of a sentence, splits it into multiple words, applies the first function to each word, and then returns a new string of the processed sentence.

```python
sentence = "Four score and seven years ago our fathers brought forth, on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal."

print(process_sentence(sentence))

# would print:
# FOUR score AND seven years AGO OUR fathers brought forth, ON THIS continent, A NEW nation, conceived IN liberty, AND dedicated TO THE proposition THAT ALL MEN ARE created equal.

# hint: sentence.split() & " ".join(word_list)
```

* Now prompt the user for an input and print the processed string.
