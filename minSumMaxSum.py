#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
arr = {}
def miniMaxSum(arr):
    # Write your code here
    arrSize = len(arr)
    summation = []
    for j in range(arrSize):
        hold = arr.pop(0)
        sum1 = 0
        for i in range(arrSize - 1):
            sum1 += arr[i]
        arr.append(hold)
        summation.append(sum1)
    # print(summation, " = ", sum1)
    print(min(summation), max(summation))

#
#if __name__ == '__main__':
#    for i in range(5):
#        arr[i] = random.randint(0, 99)
#    arr = list(map(int, input().rstrip().split()))
#    print(arr)
#    miniMaxSum(arr)
