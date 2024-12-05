#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'compareStrings' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING s1
#  2. STRING s2
#

def compareStrings(s1, s2):
    # Write your code here
    if get(s1) == get(s2):
        return 1
    else:
        return 0
    
def get(s1):
    stack = []
    l=r = 0
    while r < len(s1):
        if s1[r] != "#":
            stack.append(s1[r])
        else:
            stack.pop()
        l+=1
        r+=1
    return ''.join(stack)
        
        
            
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s1 = input()

    s2 = input()

    result = compareStrings(s1, s2)

    fptr.write(str(result) + '\n')

    fptr.close()
