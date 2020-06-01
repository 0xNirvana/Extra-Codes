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

decode_input = 'YRIRY GJB CNFFJBEQ EBGGRA'


for i in range(len(string.ascii_uppercase)):
	decode_output = rotation(decode_input, i)

	if (re.findall('LEVEL TWO PASSWORD (.*)', decode_output)):
		print re.findall('LEVEL TWO PASSWORD (.*)', decode_output)[0]
		break
# print rotation(decode_input, 13)

# print decode_output
