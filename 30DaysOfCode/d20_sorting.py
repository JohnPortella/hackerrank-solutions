#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    swaps = []

    for round in range(1,n+1):
        number_of_swaps = 0
        for index in range(0, n-1):
            if a[index] > a[index + 1]:
                a[index], a[index + 1] = a[index + 1], a[index] 
                number_of_swaps += 1
                
        if number_of_swaps == 0:
            break
            
        swaps.append(number_of_swaps)

    print(f"Array is sorted in { sum(swaps) } swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[n-1]}")
