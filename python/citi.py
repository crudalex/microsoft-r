import os

import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_historical(symbol: str):
    url = 'https://www.nasdaq.com/symbol/%s/historical' % symbol
    css = '#quotes_content_left_pnlAJAX > table'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml')
    table = soup.select(css).pop()

    df: pd.DataFrame = pd.read_html(str(table), header=0, index_col=0).pop()
    df.columns = ['Open', 'High', 'Low', 'Last', 'Volume']
    df = df.dropna(0)

    return df


if __name__ == '__main__':

    citi: pd.DataFrame = ()

    datafile = os.path.join(os.getcwd(), 'data', 'citi.csv')
    if not os.path.exists(datafile):
        citi = get_historical('c')
        citi.to_csv(datafile)
    else:
        citi = pd.read_csv(datafile, index_col=0, header=0)
