#!/usr/bin/env python3
import time

import requests

url = 'http://racing.hkjc.com/racing/info/meeting/Results/English/'
html = requests.get(url).text

from lxml import etree

selector = etree.HTML(html)

base_url = 'http://racing.hkjc.com/racing/info/meeting/Results/English/'
xpath = '//*[@id="raceDateSelect"]/option/@value'
race_dates = selector.xpath(xpath)
race_urls = [base_url + date for date in race_dates]
race_urls = [url for url in race_urls if 'Local' in url]

import re
import os

workdir = os.getcwd()
datadir = os.path.join(workdir, 'data', 'races')
if not os.path.exists(datadir):
    os.mkdir(datadir)

start_time = time.time()
for u in race_urls:
    html = requests.get(url).text
    filename = re.sub('\W+', '_', url.rstrip().lower()) + '.html'
    outfile = os.path.join(datadir, filename)
    with open(outfile, 'w', encoding='utf8') as out:
        out.write(html)
end_time = time.time()
print("Single threaded time: %s" % str(end_time - start_time))


def grab_url(url):
    html = requests.get(url).text
    filename = re.sub('\W+', '_', url.rstrip().lower()) + '.html'
    outfile = os.path.join(datadir, filename)
    with open(outfile, 'w', encoding='utf8') as out:
        out.write(html)


from multiprocessing.dummy import Pool as ThreadPool
#from multiprocessing import Pool as ThreadPool

pool = ThreadPool(8)
start_time = time.time()
pool.map(grab_url, race_urls)
pool.close()
pool.join()
end_time = time.time()
print("Multi threaded time: %s" % str(end_time - start_time))
