# ----------------------------
# Median of Two Sorted Arrays
# ----------------------------
#
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# -----------
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# ----------
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
# Example 3:
# ----------
# Input: nums1 = [0,0], nums2 = [0,0]
# Output: 0.00000
#
# Example 4:
# ----------
# Input: nums1 = [], nums2 = [1]
# Output: 1.00000
#
# Example 5:
# ----------
# Input: nums1 = [2], nums2 = []
# Output: 2.00000
#
# ---------
# Solution
# ---------
# //: divide with integral result (discard remainder)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged_array = nums1 + nums2
        merged_array.sort()
        length_merged_array = len(merged_array)

        if length_merged_array % 2 == 0:
            median1 = merged_array[length_merged_array//2]
            median2 = merged_array[(length_merged_array // 2) - 1]
            median = float(median1 + median2) / float(2)
        else:
            median = merged_array[length_merged_array // 2]

        return median


p1 = Solution()
item1 = [1, 2]
item2 = [3, 4]

print(p1.findMedianSortedArrays(item1, item2))

