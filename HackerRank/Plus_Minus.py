'''
--------------------
Plus Minus
--------------------
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems. The test cases are scaled to six decimal places,
though answers with absolute error of up to 10 -4 are acceptable.

Example
--------
arr = [1, 1, 0, -1, -1]
There are n = 5  elements, two positive, two negative and one zero. Their ratios are ,  and . Results are printed as:

2/5 = 0.400000, 2/5 = 0.400000, 1/5 = 0.200000

0.400000
0.400000
0.200000

Function Description
--------------------
Complete the plusMinus function in the editor below.

plusMinus has the following parameter(s):

int arr[n]: an array of integers

Print

Print the ratios of positive, negative and zero values in the array.
Each value should be printed on a separate line with 6 digits after the decimal.
The function should not return a value.

Input Format

The first line contains an integer,n , the size of the array.
The second line contains n space-separated integers that describe arr[n].

Constraints
-----------

0 < n <= 100
-100 <= arr[i] <= 100

Output Format
-------------
Print the following 3 lines, each to 6 decimals:

1. proportion of positive values
2. proportion of negative values
3. proportion of zeros

Sample Input
----------------
STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

Sample Output

0.500000
0.333333
0.166667

Explanation
----------
There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
The proportions of occurrence are positive: 3/6 = 0.500000 , negative: 2/6 = 0.333333 and zeros: 1/6 = 0.166667.

'''
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
    no_of_element = len(arr)
    no_of_positive_number = 0
    no_of_negative_number = 0
    no_of_zero = 0
    for i in arr:
        if i == 0:
            no_of_zero += 1
        elif i > 0:
            no_of_positive_number += 1
        elif i < 0:
            no_of_negative_number += 1

    print("{:.6f}".format((no_of_positive_number/no_of_element)))
    print("{:.6f}".format((no_of_negative_number / no_of_element)))
    print("{:.6f}".format((no_of_zero / no_of_element)))


if __name__ == '__main__':
    # n = int(input().strip())
    #
    # arr = list(map(int, input().rstrip().split()))
    arr = [-4, 3, -9, 0, 4, 1]
    # arr = [1, 1, 0, -1, -1]
    plusMinus(arr)
