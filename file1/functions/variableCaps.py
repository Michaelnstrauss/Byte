#!/usr/bin/env

def process_word(word):
    if len(word) <= 4:
        return word.upper()
    else:
        return word.lower()

word = 'bumbleBEE'


def process_sentence(sentence):
    new_list = []
    split_sentence = sentence.split()
    for s_split in split_sentence:
        new_list.append(process_word(s_split))
    return " ".join(new_list)
#   split_sentence = join_sentence.split()
#   join_sentence = "".join(sentence)
#   return process_word(split_sentence)
#   return process_word(sentence)


sentence = 'Four score and seven years ago our fathers brought forth, on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.'


if __name__=='__main__':
    print(process_sentence(sentence))
