# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import minSumMaxSum as minmax
import PlusMinusZero as pmz
import random

lis = []
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(5):
        t = random.randint(0, 99)
        lis.append(t)
        print(t, lis)
    print("list value: ", lis)
    arr = list(map(int, input().rstrip().split()))
    print("array value: ", arr)
    minmax.miniMaxSum(arr)
    pmz.plusMinus(arr)
    print("End")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
