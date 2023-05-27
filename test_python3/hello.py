#!/usr/bin/env python3

"""
This file uses only built-in capabilities for Python3
"""

import sys

import argparse
parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-t", "--trace", action="store_true", help="trace calls and returns")
args = parser.parse_args()
#print("args=",vars(args))

if vars(args)['trace']:
    sys.settrace(mytrace)

print("hello")

def myfunc(x):
    print(x+1)
    return "a"

myfunc(5)

