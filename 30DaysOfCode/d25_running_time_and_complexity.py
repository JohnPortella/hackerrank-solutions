# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

def is_prime(value):
    
    if value == 1:
        print('Not prime')
    elif value == 2:    
        print('Prime')
    elif value % 2 == 0 or value % 3 == 0:
        print('Not prime')
    elif value < 100000000:        
        mersenne = (2**value-1) % value
        print('Prime' if mersenne == 1 else 'Not prime')
    else:
        for i in range(2,int(math.sqrt(value))+1):
            if value%i == 0:
                print("Not prime")
                break
        else:
            print('Prime')

n = int(input())

for _ in range(n):    
    is_prime(int(input()))
    
