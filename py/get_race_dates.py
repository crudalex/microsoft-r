#!/usr/bin/env python3
import datetime
import os
import sqlite3

import pandas as pd
import requests
from multiprocessing import Pool as ThreadPool, cpu_count
from lxml import etree


def get_race_urls(base_url):
    html = requests.get( base_url ).text
    selector = etree.HTML( html )

    xp = '//*[@id="raceDateSelect"]/option/@value'
    values = selector.xpath( xp )
    urls = [base_url + i for i in values if 'Local' in i]

    return urls


def grab_race_htmls(url):
    html = requests.get( url ).text.replace( '\r\n', '\n' )
    return html


if __name__ == '__main__':
    baseurl = 'http://racing.hkjc.com/racing/info/meeting/Results/English/'
    race_urls = get_race_urls( baseurl )

    pool = ThreadPool( cpu_count() )
    results = pool.map( grab_race_htmls, race_urls )
    race_htmls = list( results )

    dbdir = os.path.join( os.getcwd(), 'data', 'sqlite3')
    if not os.path.exists( dbdir ) :
        os.mkdir( dbdir)
    dbfile = os.path.join( dbdir, 'racing.db' )

    try:
        conn = sqlite3.connect( dbfile )
        df = pd.DataFrame()
        df['url'] = pd.Series( race_urls )
        df['html'] = pd.Series( race_htmls )
        df.set_index('url')
        df.to_sql( name='retrieved_url', con=conn, if_exists='append', index = False)
    except sqlite3.IntegrityError as e:
        pass

    pool.close()
    pool.join()
