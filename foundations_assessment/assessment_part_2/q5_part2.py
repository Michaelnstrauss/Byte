

string1 = input("Input a string, 'done' to quit: ")

def string_func(string1):
    if string1 != 'done': 
        while True:       
            try:
                list_words = []
                for letters in string1.split():
                    list_words += letters
                join_letters = list_words[0] + list_words[1]
                print(join_letters)
            except IndexError:
                for letter in string1.split():
                    print(letter)
        input('are you done? enter done if so')
            break
    else:
        break
    
    
    #            print(letters)
    #        return letters


string_func(string1)