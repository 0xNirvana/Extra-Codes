#!/usr/bin/env python

import requests
import re

username='natas8'
password='DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe'

#cookie = { "loggedin" : "1" }
url = 'http://%s.natas.labs.overthewire.org/' %username
#session = requests.Session()
path = 'index-source.html'
# response = requests.get(url, auth = (username, password))
response = requests.post(url, data={'secret':'oubWYf2kBq', 'submit':'submit'}, auth = (username, password))
content = response.text

# print content

print re.findall('The password for natas9 is (.*)', content)[0]
# The password was stored as an encoded string in the source code, all that was to be done was to write a code to reverse those operation.
# Another natas8 php file is present containing that code