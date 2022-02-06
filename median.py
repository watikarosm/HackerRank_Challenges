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
    numSet = random.randint(0, 50000)   # creating a random size of the set from 0 to 50000
    for i in range(numSet+1):
        h = random.randint(-9999, 9999)     # get a random value from -9999 to 9999
        array2.append(h)                # add the value above in to the array
    print(array2)
    median(array)               # case 0: small set with fixed values
    median(array1)              # case 1: small set with fixed and repeated values
    median(array2)              # case 2: random size set with random values
    median(array3)              # case 4: empty set

