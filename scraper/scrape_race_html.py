#!/usr/bin/env python3

import requests
import re
import os

xpaths = {
    'date_and_track': '//*[@id="results"]/div[3]/table/tbody/tr/td[1]'
    'race_day_and_year': '//*[@id="results"]/div[5]/div[1]'
    'class': '//*[@id="results"]/div[5]/div[2]/table/tbody/tr[1]/td[1]/text()'
    'length': '//*[@id="results"]/div[5]/div[2]/table/tbody/tr[1]/td[1]/span'
    'going': '//*[@id="results"]/div[5]/div[2]/table/tbody/tr[1]/td[3]'
    'course': '//*[@id="results"]/div[5]/div[2]/table/tbody/tr[2]/td[3]'
    'section_time': '//*[@id="results"]/div[5]/div[2]/table/tbody/tr[4]/td[2]'
    'horse_jockey_trainer': '//*[@id="results"]/div[6]/table[2]'
}
