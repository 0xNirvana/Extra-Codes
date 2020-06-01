#!/usr/bin/env python

import string
import re
import collections


def rotation (input, rot_val):
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)

	upper.rotate(rot_val)
	lower.rotate(rot_val)

	upper = ''.join(upper)
	lower = ''.join(lower)

	
	return input.translate(string.maketrans(string.ascii_lowercase, lower)).translate(string.maketrans(string.ascii_uppercase, upper))

decode_input = 'OMQEMDUEQMEK'


for i in range(len(string.ascii_uppercase)):
	rotation(decode_input, i)				#Add print to this statement to get all the values


print rotation(decode_input, 12)
# decode_output=rotation(decode_input, 5)

# print decode_output
