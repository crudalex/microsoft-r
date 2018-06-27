#!/usr/bin/env python3

import io
import requests
import re
import os
from multiprocessing import Pool as ThreadPool
import multiprocessing
from lxml import etree

workdir = os.getcwd()
datadir = os.path.join( workdir, 'data', 'racing' )
if not os.path.exists( datadir ):
    os.mkdir( datadir )


def get_race_urls(base_url):
    html = requests.get( base_url ).text
    selector = etree.HTML( html )
    race_xpath = '//*[@id="raceDateSelect"]/option/@value'
    race_dates = selector.xpath( race_xpath )
    race_urls = [base_url + d for d in race_dates]
    race_urls = [url for url in race_urls if 'Local' in url]
    return race_urls


def grab_race_htmls(url):
    html = requests.get( url ).text.replace( '\r\n', '\n' )
    return html


if __name__ == '__main__':
    baseurl = 'http://racing.hkjc.com/racing/info/meeting/Results/English/'
    race_urls = get_race_urls( baseurl )

    pool = ThreadPool( multiprocessing.cpu_count() )
    results = pool.map( grab_race_htmls, race_urls )
    race_htmls = list( results )

    for url, html in zip( race_urls, race_htmls ):
        filename = re.sub( '\W+', '_', url ).rstrip().lower() + '.html'
        htmldir = os.path.join( datadir, 'html' )
        if not os.path.exists( htmldir ):
            os.mkdir( htmldir )

        outfile = os.path.join( htmldir, filename )
        with io.open( outfile, 'w', encoding='utf8' ) as f:
            f.write( html )

    pool.close()
    pool.join()
