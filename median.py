import numpy as np
import random

def median(arr):
    print(arr)
    arr.sort()
    print(arr)
    j = len(arr)
    print(j)
    if j % 2 == 0:  # odd case
        k = int((j + 1) / 2)
        #        print(k)
        #        l = (array[k-1] + array[k])/2
        print((arr[k - 1] + arr[k]) / 2, " is the median.")
    else:  # even case
        k = int(j/2)
        print(arr[k], " is the median")

if __name__ == '__main__':
    array = [1, 3, 2, 5, 4, 7, 6]
    array1 = [2, 3, 8, 2, 4, 1, 5, 7]
    array2 = []
    numSet = random.randint(1, 9)
    for i in range(numSet+1):
        j = random.randint(0, 99)
        array2.append(j)
    print(array2)
    median(array)
    median(array1)
    median(array2)

