

#print char(65) to char(78) on one line
#and char(78) to char(90) on line two


rows_letter = ''
for char_number in range(65,78):
    letter = chr(char_number)
    rows_letter += letter + ' '
print(rows_letter)

rows_letter_2 = ''
for char_number_2 in range(78,91):
    letter = chr(char_number_2)
    rows_letter_2 += letter + ' '
print(rows_letter_2)