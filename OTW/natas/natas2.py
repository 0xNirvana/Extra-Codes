#!/usr/bin/env python

import requests
import re

username='natas2'
password='ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi'
path= 'files/users.txt'
url = 'http://%s.natas.labs.overthewire.org/' %username
response = requests.get(url + path, auth = (username, password))
content = response.text

# print content  

print re.findall('natas3:(.*)', content)[0]


#There was a 1X1 pixel image on the page and it's source path was mentioned. So, the idea was to check the files present in the folder in which the image was also present.