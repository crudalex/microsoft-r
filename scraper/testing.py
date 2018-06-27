#!/usr/bin/env python3

import math
from urllib import request
import re

num = math.sqrt(16)
num

string = 'xxxx x x xxx x askldcfaslc x x x x xxx dsaflasd lksdfsa x daskjfl sdakljad sfxvlzcj'

re.findall('x+', string)
re.findall('a\w+c', string)
re.findall('a\w+?c', string)

if re.search("dog", "the dog was lying on the couch"):
    print('helloworld')

re.findall("at", "the cat was sat on the mat")

re.sub("ham", "beef", "Beth ate a hamburger in her hammock")

m = re.search("dog", "(dog)%", flags=re.IGNORECASE | re.MULTILINE)
print(m.group(0))

email = 'crudalex@gmail.com'
m = re.search('(.*)@(.*)', email)
if m:
    m.group(1)
    m.group(2)

s = re.sub('(.*)@gmail.com','atwlam@gmail.com', email )
print(s)


import requests
url = 'http://racing.hkjc.com/racing/info/meeting/Results/English/'
r = requests.get(url)
r.content
r.text

