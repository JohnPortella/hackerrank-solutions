# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

#inputs
n = int(input())
words = (input()).split(" ")
length = int(input())
# business
combs = list(combinations(enumerate(words), length))
contain_a = 0
for pair in combs:
    contain = False
    for i in range(len(pair)):
        if pair[i][1] == 'a':
            contain = True
            break
    if contain:
        contain_a += 1        
#output    
print(round(contain_a/len(combs),4))
