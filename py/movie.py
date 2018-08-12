#!/usr/bin/env python3

import os

import pandas as pd

data = pd.read_table(os.path.join('data', 'ml-100k', 'u.data'), sep='\t', names=None, encoding='latin-1', header=None)
user = pd.read_table(os.path.join('data', 'ml-100k', 'u.user'), sep='|', names=None, encoding='latin-1', header=None)
item = pd.read_table(os.path.join('data', 'ml-100k', 'u.item'), sep='|', names=None, encoding='latin-1', header=None)

data.columns = 'userid|itemid|rating|timestamp'.split("|")
user.columns = 'userid|age|gender|occupation|zipcode'.split("|")
item.columns = 'movie_id|movie_title|release_date|video_release_date|imdburl|unknown|action|adventure|animation|childrens|comedy|crime|documentary|drama|fantasy|film-noir|horror|musical|mystery|romance|sci-fi|thriller|war|western'.split(
    "|")
mean_r = pd.pivot_table(data, values='rating', index='userid', aggfunc='mean')

merged_r = pd.merge(user, mean_r, on='userid')

std_r = pd.pivot_table(merged_r, values='rating', index='gender', aggfunc='std')

print("Gender")
print("M %.2f" % std_r.loc['M'])
print("F %.2f" % std_r.loc['F'])
