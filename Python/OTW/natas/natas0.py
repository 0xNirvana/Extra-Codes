#!/usr/bin/env python

import requests				#Package to generate different types of HTTP requests
import re 					#Package to perform regex operations

username='natas0'
password=username

url = 'http://%s.natas.labs.overthewire.org/' %username
response = requests.get(url, auth = (username, password))
content = response.text

# print content

print re.findall("<!--The password for natas1 is (.*) -->", content)[0]			# The [0] here means the first matched item