#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    index_x, index_y = 0,0
    
    all_hourglasses = []
    while index_x < 4 and index_y < 4:
        
        sub_arr = [ row[index_x:index_x+3] for row in arr[index_y:index_y+3]]
        total_sum = sum(value for row in sub_arr for value in row)
        hourglasses  = total_sum - sub_arr[1][0] - sub_arr[1][2]
        all_hourglasses.append(hourglasses)
        
        if index_x < 3 and index_y < 3:
            index_x, index_y = index_x + 1, index_y
        elif index_x == 3 and index_y < 3:
            index_x, index_y = 0, index_y + 1
        elif index_x < 3 and index_y == 3:
            index_x, index_y = index_x + 1, index_y
        else:
            index_y += 1
    
    print(max(all_hourglasses))
