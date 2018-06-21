#!/usr/bin/env python

import os
import pandas as pd

workdir = os.getcwd()
datadir = os.path.join(workdir, "data")
csvfile = os.path.join(datadir, 'cameras.csv')

if not os.path.exists(datadir):
    os.mkdir(path = datadir)
    print("Directory '%s' created." % datadir)
    os.listdir(datadir)

import ssl
print(ssl.OPENSSL_VERSION)

import urllib
url = 'https://data.baltimorecity.gov/api/views/dz54-2aru/rows.csv?accessType=DOWNLOAD'
urllib.request.urlretrieve(url=url, filename=csvfile)

import datetime
now = datetime.datetime.now()

# read in flat file
cameraDF = pd.read_table(csvfile, header=0, sep=",")
cameraDF.head(5)

# read in csv
cameraDF2 = pd.read_csv(csvfile, quotechar='"')
cameraDF2.head(5)

# read in excel file
excelfile = os.path.join(datadir, 'cameras.xlsx')
cameraDF3 = pd.read_excel(excelfile, sheet_name=0, header=0)
