#!/usr/bin/python
# -*- coding: utf-8 -*-

def solve_it(input_data):
    # return a positive integer, as a string
    return str(abs(hash(input_data)))

if __name__ == '__main__':
    print('This script submits the integer: %s\n' % solve_it('-1000'))

