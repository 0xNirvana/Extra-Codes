#!/usr/bin/env python

import string

key = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN"
input = "PNUKLYLWRQKGKBE"
alphabets = string.ascii_uppercase



# print alphabets
# print key
# print input

output = ''
for i in range(len(input)):
	char_input = input[i]
	char_key = key[i]
	# print char_input, "-", char_key, " = "
	value = alphabets.index(char_input) - alphabets.index(char_key) 
	# print value
	output += alphabets[value]

print output
