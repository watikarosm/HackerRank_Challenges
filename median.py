import numpy as np
import random


def median(arr):
    print(arr)
    arr.sort()
    print(arr)
    j = len(arr)
    print(j)
    if j == 0:
        print("This is an empty set.")
    elif j % 2 == 0:  # even case
        k = int((j + 1) / 2)
        print((arr[k - 1] + arr[k]) / 2, " is the median.")
    else:  # odd case
        k = int(j/2)
        print(arr[k], " is the median")


if __name__ == '__main__':
    array = [1, 3, 2, 5, 4, 7, 6]
    array1 = [2, 3, 8, 2, 4, 1, 5, 7]
    array2 = []
    array3 = []
    numSet = random.randint(0, 50000)
    for i in range(numSet+1):
        h = random.randint(-9999, 9999)
        array2.append(h)
    print(array2)
    median(array)
    median(array1)
    median(array2)
    median(array3)

