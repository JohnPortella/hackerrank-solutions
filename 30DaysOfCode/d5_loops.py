#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    for index in range(1,11):
        print(f"{n} x {index} = {n*index:d}")
