#!/usr/bin/env python

import requests
import re
import urllib
import base64

username='natas11'
password='U82q5TCMMQ9xuFoI3dYX61s7OZD9JKoK'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = 'index-source.html'
cookie = { 'data':'ClVLIh4ASCsCBE8lAxMacFMOXTlTWxooFhRXJh4FGnBTVF4sFxFeLFMK' }
session = requests.session()
response = session.get(url, cookies=cookie, auth=(username, password))
content = response.text
# print content
# print response.cookies['data']
print "Base 64 decoded cookie in Hex: " + base64.b64decode(urllib.unquote(response.cookies['data'])).encode('hex')
print "Password is: " + re.findall('The password for natas12 is (.*)<br>', content)[0]



# There was nothing but just to reverse engineer the function written in there.
# The function calculated the cookie value and we just need to reverse ut.