

A = ord('A')
dic = {}

for code in range(A+25, A-1, -1):
    letter = chr(code)
    dic[letter] = code


for key, value in dic.items():
    print(key,value)


    # letter_num = None
    # letter_num += key,value