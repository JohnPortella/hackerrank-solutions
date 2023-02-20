#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    
    gmail_names = []
    for N_itr in range(N):
        first_multiple_input = input().rstrip()

        # code
        pattern = r'(\w+)\s(\w+(\.\w+)*@\w+(\.\w+))'
        match = re.search(pattern, first_multiple_input)

        name = match.group(1)
        email = match.group(2)
        nickname, company_domain = email.split("@")
        company, domain = re.search(r'(\w+)\.(\w+)', company_domain).groups()
        
        if company == "gmail":
            gmail_names.append(name)
    
    gmail_names.sort()
    for name in gmail_names:
        print(name)
            
