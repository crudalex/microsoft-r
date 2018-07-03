import requests
import pandas as pd
from bs4 import BeautifulSoup


def get_dji(filename: str):
    url = 'http://money.cnn.com/data/dow30/'
    x = '//*[@id="wsod_indexConstituents"]/div/table'
    selector = '#wsod_indexConstituents > div > table'

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'lxml', from_encoding=r.encoding)
    table = soup.select(selector).pop().__str__()

    df1 = pd.read_html(table, header=0).pop()
    df2 = df1.Company.str.split('\s+', n=1, expand=True)
    df2.columns = ['Code', 'Company Name']
    df3 = df1.merge(df2, left_index=True, right_index=True)
    df4 = df3.set_index(df3.Code)

    return df4


if __name__ == '__main__':

    import os

    dji = pd.DataFrame()

    filename = os.path.join(os.getcwd(), 'data', 'dji.csv')

    if not os._exists(filename):
        dji = get_dji(filename)
        dji.to_csv(filename)
    else:
        dji = pd.read_csv(filename, header=0, index_col=0)

    print(dji)

