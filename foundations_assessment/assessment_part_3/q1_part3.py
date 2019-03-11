from collections import Counter
import csv

def count_lines():
    total_lines = 0
    with open('tothelighthouse.txt', 'r') as house_file:
        for line in house_file:
            # number_line = len(lines)
            total_lines += 1
        print(total_lines)


def new_text_file():
    len_list = []
    with open('tothelighthouse.txt', 'r') as house_file:
        for line in house_file:
            len_line = len(line)
            len_list.append(len_line)
    with open('linecount.txt', 'w') as new_file:
        for num in len_list:
            new_file.write("{}\n".format(str(num)))
            
    
new_text_file() 
    
    # with open('linecount.txt', 'w+') as new_file:
    #     for new_file in count_lines():
    #         return new_file


# print(new_text_file(count_lines))



