'''

--------------------
Diagonal Difference
--------------------

Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9

The left-to-right diagonal = 1 + 5 + 9 = 15 .
The right to left diagonal = 3 + 5 +9 = 17 .
Their absolute difference is |15 - 17 | = 2 .

Function description
-------------------
Complete the  diagonalDifference function in the editor below.

diagonalDifference takes the following parameter:

int arr[n][m]: an array of integers

Return
----------
int: the absolute diagonal difference

Input Format
------------
The first line contains a single integer, n, the number of rows and columns in the square matrix arr.
Each of the next n lines describes a row,a[i] , and consists of n space-separated integers arr[i][j] .

Constraints
------------
-100 <= arr[i][j] <= 100

Output Format
-------------
Return the absolute difference between the sums of the matrix's two diagonals as a single integer.


Sample Input
--------------

3

11  2  4
4   5  6
10  8 -12

Sample Output
-------------
15

Explanation
--------------
The primary diagonal is:

11
   5
     -12

Sum across the primary diagonal: 11 + 5 - 12 = 4

The secondary diagonal is:

     4
   5
10

Sum across the secondary diagonal: 4 + 5 + 10 = 19

Difference: |4 - 19| = 15

'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    counter = len(arr) - 1
    left_to_right_diagonal = []
    right_to_left_diagonal = []

    for i in range(len(arr)):
        left_to_right_diagonal.append(arr[i][i])
        right_to_left_diagonal.append(arr[i][counter])
        counter -= 1

    # for i in range(len(arr)):
    #     right_to_left_diagonal.append(arr[i][counter])
    #     counter -= 1

    return abs(sum(left_to_right_diagonal) - sum(right_to_left_diagonal))


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # n = int(input().strip())
    #
    # arr = []
    #
    # for _ in range(n):
    #     arr.append(list(map(int, input().rstrip().split())))

    arr = [[1, 2, 3], [4, 5, 6], [9, 8, 9]]
    # arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    result = diagonalDifference(arr)
    print(result)

    #
    # fptr.write(str(result) + '\n')
    #
    # fptr.close()
