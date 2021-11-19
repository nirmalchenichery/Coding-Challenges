# -----------------------
# Remove Duplicates from Sorted Array
# -----------------------
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum
# and return its sum.
#
# A subarray is a contiguous part of an array.

# Example 1:
# ----------
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# -----------
# Input: nums = [1]
# Output: 1
#
# Example 3:
# -------------
# Input: nums = [5,4,-1,7,8]
# Output: 23

# ---------
# Solution
# ---------

class Solution:
    def maxSubArray(self, nums):
        element_total = 0
        maximum_sum = -999999999

        for i in nums:
            element_total += i
            maximum_sum = max(maximum_sum, element_total)
            if element_total < 0:
                element_total = 0

        return maximum_sum;


# nums = [-2,1,-3,4,-1,2,1,-5,4]
# nums = [1]
nums =[5,4,-1,7,8]
# nums = [-1]
p1 = Solution()
print(p1.maxSubArray(nums))
