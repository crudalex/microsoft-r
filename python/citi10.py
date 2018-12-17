import os

import pandas as pd

if __name__ == '__main__':
    datafile = os.path.join(os.getcwd(), 'data', 'citi10.csv')
    citi = pd.read_csv(datafile, index_col=0, header=0, parse_dates=True)
    citi.sort_index(inplace=True)

