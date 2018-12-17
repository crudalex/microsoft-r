#!/usr/bin/env python3

import math
import re
import requests

num = math.sqrt(16)

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

s = re.sub('(.*)@gmail.com', 'atwlam@gmail.com', email)
print(s)

url = 'https://cn.bing.com/search'
kw = {'q': 'hello world'}
r = requests.post(url, params=kw)

print(r.content)
print(r.text)
print(r.url)

import json

url = 'https://www.apple.com/hk/shop/updateSummary?node=home/shop_iphone/family/iphone_x&step=select&product=MQA82ZP%2FA&carrierPolicyType=UNLOCKED'
j = requests.get(url).text

v = json.load(j)

a = ['alex', 'lam']
d = ['daniel', 'cheung']
k = ['kc', 'tam']
s = ['sai', 'li']
l = ['alex', 'lam']


e = [ a, d, k, s, l]

set(e)