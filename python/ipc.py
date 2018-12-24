#!/usr/bin/env python3

'''Demo multi process producer/consumer FIFO'''

import os
import time
import sys
import random

FIFO_DEV = '/tmp/pipefifo'                       # must open same name

def producer():
    '''producer'''
    pipeout = open(FIFO_DEV, 'w')     # open fifo pipe file as fd
    while True:
        n = random.randint(1, 100)
        msg = ('%d\n' % n)    # binary as opened here
        pipeout.write(msg)
        try:
            pipeout.flush()
        except BrokenPipeError as e:
            # pipeout.close()
            exit()
        # time.sleep(1)

def consumer():
    '''consumer'''
    pipein = open(FIFO_DEV, 'r')                 # open fifo as text file object
    while True:
        n = int(pipein.readline())           # blocks until data sent
        print('%d received "%s"' % (os.getpid(), n))
        if n % 11 == 0:
            print('consumer %d exiting' % os.getpid())
            pipein.close()
            exit()

if __name__ == '__main__':
    if not os.path.exists(FIFO_DEV):
        os.mkfifo(FIFO_DEV)                      # create a named pipe file

    if len(sys.argv) == 1:
        for i in range(3): 
            pid = os.fork()
            if pid == 0: 
                consumer()                                 # run as consumer if no args
    else:                                        # else run as producer process
        producer()

    os.wait()

