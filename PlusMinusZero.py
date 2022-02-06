#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    arrSize = len(arr)
    negative = 0
    positive = 0
    zero = 0
    ratio = 0.00
    for i in range(len(arr)):
        if arr[i] < 0:
            negative += 1
        elif arr[i] > 0:
            positive += 1
        else:
            zero += 1
    print("{:.6f}".format(positive / arrSize))
    print("{:.6f}".format(negative / arrSize))
    print("{:.6f}".format(zero / arrSize))

#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     plusMinus(arr)
