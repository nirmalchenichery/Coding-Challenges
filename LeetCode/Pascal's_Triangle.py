# ----------------------------
# 118. Pascal's Triangle
# ----------------------------
# URL :- https://leetcode.com/problems/pascals-triangle/

# Given an integer numRows, return the first numRows of Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 #     1
 #    1  1
 #   1  2  1
 #  1  3  3  1
 # 1  4  6  4  1

# Example 1:
# ----------
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# ----------
# Input: numRows = 1
# Output: [[1]]

# ---------
# Solution
# ---------

class Solution(object):
    def generate(self, numRows):
        result = [[1]]
        for i in range(numRows-1):
            temp = [0] + result[-1] + [0]
            newRow = []
            for j in range(len(result[-1]) + 1 ):
                newRow.append(temp[j] + temp[j+1])

            result.append(newRow)

        return result


numRows = 5
p1 = Solution()
print(p1.generate(numRows))