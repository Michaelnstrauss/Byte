
def single_letter_count(sen1='bubble', sen2='l'):
    if sen2 in sen1:
        return sen1.count(sen2)
    return "mistake"
    
print(single_letter_count('boo','l'))