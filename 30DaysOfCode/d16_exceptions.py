#!/bin/python3

import sys
import numbers


S = input()

try:
    print (int(S))
except ValueError:
    print ("Bad String")
