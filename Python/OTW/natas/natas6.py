#!/usr/bin/env python

import requests
import re

username='natas6'
password='aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1'

url = 'http://%s.natas.labs.overthewire.org/' %username

path = "includes/secret.inc"
# response = requests.get(url, auth = (username, password))
response = requests.post(url, auth = (username, password), data={'secret':'FOEIUWGHFEEUHOFUOIU', 'submit':'submit'})
content = response.text

# print content

print re.findall('The password for natas7 is (.*)', content)[0]


# On the homepage there is an option to "View Sourcecode" and over there is a file secret.inc file included having the secret value that is to be entered at the homepage
# We need to pass that secret value using post method

# In the form there are 2 inputs: 1. secret and 2. submit
# That's why secret and submit, two parameters are passed in the data part of post request