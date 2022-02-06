#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime
#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    print(s[-2:])
    t = int(s[:2])+12
    print(t)
    print(s[:-2])
    print("00" + s[2:8])
    t = str(t)
    if s[-2:] == "PM" and s[:2] == "12":
        return s[:-2]
    elif s[-2:] == "PM":
        return t+s[2:8]
    elif s[-2:] == "AM" and s[:2] == "12":
        return "00" + s[2:8]
    elif s[-2:] == "AM":
        return s[:-2]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
