from itertools import product
#import numpy as np

first_line = list(map(int,input().split(" ")))
k,m = first_line[0], first_line[1]

if not 1 <= k <= 7 or not 1 <= m <= 1000:
    raise Exception('k or m value is invalid')

array_values = []
for _ in range(k):
    #row = np.array( [list(map(int,input().split(" ")))[1:]] )
    #row = row ** 2
    row = list(map(lambda x: int(x) ** 2,input().split(" ")))        
    array_values.append(row[1:])

mods = [ sum(values) % m for values in list(product(*array_values))]
print(max(mods))
