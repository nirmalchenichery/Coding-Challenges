# ----------------------------
# 35. Search Insert Position
# ----------------------------

# Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# -----------
# Input: nums = [1,3,5,6], target = 5
# Output: 2
#
# Example 2:
# ----------
# Input: nums = [1,3,5,6], target = 2
# Output: 1
#
# Example 3:
# ---------
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#
# Example 4:
# ----------
# Input: nums = [1,3,5,6], target = 0
# Output: 0
#
# Example 5:
# -----------
# Input: nums = [1], target = 0
# Output: 0

# ---------
# Solution
# ---------

class Solution:
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        for i in nums:
            if i > target:
                return nums.index(i)
        return len(nums)

# nums = [1, 3, 5, 6]
# target = 5
# nums = [1, 3, 5, 6]
# target = 7
nums = [1, 3, 5, 6]
target = 2

p1 = Solution()
print(p1.searchInsert(nums, target))