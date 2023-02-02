#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    n_bin = (bin(n))[2:]
    parts = n_bin.split("0")
    max_number = max([ len(part) for part in parts])
    print(max_number)
