import math
import os
import random
import re
import sys
import time
from datetime import datetime

def timeSturture(s):
    # Write your code here
    t = datetime.today()
    j = 0
    for i in s:
        print("{}. ".format(j), i, " ", s[i:])
        j += 1
    localTime = time.asctime(s)
    print(s[-2:], "local time: %p", localTime)
    print("Datetime function: %s" % t.strftime("%I:%M:%S %p"))
    print("Time function: %p", s[2:])
    print("Done Printing...")

def timeConversion12_24(s):
    pass

def timeConversion24_12(s):
    # Write your code here
    print(s)
    print(s[-6:-3])
    print(s[-6:-5])
    u = int(s[3])
    print(u)
    print(s[3])
    if u > 12:
        u = str(u - 12)

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # 
    s = time.localtime()
    print ("Local time: ", s)
    # 
    # result = timeConversion(s)
    # 
    # fptr.write(result + '\n')
    #
    print("Start timeStructure function: ")
    timeSturture(s)
    print("End timeStructure function: ")
    print("Start timeConversion24_12 function: ")
    timeConversion12_24(s)
    print("End timeConversion24_12 function: ")
    print("Start timeConversion24_12 function: ")
    timeConversion24_12(s)
    print("End timeConversion24_12 function: ")
    print(time.asctime(s))
 #   fptr.close()