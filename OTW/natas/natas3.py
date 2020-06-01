#!/usr/bin/env python

import requests
import re

username='natas3'
password='sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14'
path= "s3cr3t/users.txt"
url = 'http://%s.natas.labs.overthewire.org/' %username
response = requests.get(url + path, auth = (username, password))
content = response.text

# print content

print re.findall('natas4:(.*)', content)[0]


#The description says "Even google can't find", point out to the file robots.txt.
#From robors.txt we get the path to seecret folder.