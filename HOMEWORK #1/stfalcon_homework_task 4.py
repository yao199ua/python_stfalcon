# 4. Alphabet
'''
alphabet = [(range(a,z))] # FAIL :D

import string
string.ascii_lowercase
# Stackoverflow https://stackoverflow.com/questions/16060899/alphabet-range-in-python

list.ascii_lowercase

list.string(ascii_lowercase)

list(string.ascii_lowercase)
alphabet = list(string.ascii_lowercase)

alphabet
# Use ENUMERATE + f'string ???
'''

'''
index_count = 0
input('Type any letter')

while letter in alphabet:
    print('You entered (input)')
    
# by letter I mean the result of input command, ideally...

for letter in alphabet:
    print(f'The previous letter is {}. 
    The next letter is {}')

''' 
# enumerate alphabet # SyntaxError: invalid syntax
# enumerate 'alphabet' # SyntaxError: invalid syntax

letter = input('Please enter a letter: ')
letter_index = ord(letter)

print('You entered: ', letter)

if letter.lower() != 'a':
    prev_letter = chr(letter_index - 1)
    print('Previous symbol: ', prev_letter)

if letter.lower() != 'z':
    next_letter = chr(letter_index +1)
    print('Next symbol: ', next_letter)
