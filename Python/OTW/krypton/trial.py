#!/etc/bin env python

import string
import collections
import base64

def rotation(input, rot_val):
	alphabets=collections.deque(string.ascii_uppercase)
	alpha = ''.join(alphabets)
	# print alpha

	alphabets.rotate(rot_val)
	alphabets = "".join(alphabets)
	# print alphabets	

	return input.translate(string.maketrans(string.ascii_uppercase, alphabets))



for i in range(len(string.ascii_uppercase)):
	decrypted_key = rotation("OMQEMDUEQMEK", i)
	print decrypted_key


s = \xeb\x11\x5e\x31\xc9\xb1\x21\x80\x6c\x0e\xff\x01\x80\xe9\x01\x75\xf6\xeb\x05\xe8\xea\xff\xff\xff\x6b\x0c\x59\x9a\x53\x67\x69\x2e\x71\x8a\xe2\x53\x6b\x69\x69\x30\x63\x62\x74\x69\x30\x63\x6a\x6f\x8a\xe4\x53\x52\x54\x8a\xe2\xce\x81