


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    sum = 0
    for i in ar:
        sum = sum + i
    return int(sum)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # ar_count = int(input().strip())
    #
    # ar = list(map(int, input().rstrip().split()))
    ar = [1, 2, 3]
    result = simpleArraySum(ar)
    print(result)
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
