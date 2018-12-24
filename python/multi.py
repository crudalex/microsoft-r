#!/usr/bin/env python
import time

from multiprocessing.pool import ThreadPool as Pool

def run(x):
    print("Thread %d starting..." % x, flush=True)
    time.sleep(10)

if __name__ == '__main__':
    pool = Pool(10)
    pool.map(run, range(1, 512))
    pool.close()
    pool.join
