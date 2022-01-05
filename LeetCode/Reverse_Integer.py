# ---------------
# Reverse Integer
# ---------------
#
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
# ----------
# Input: x = 123
# Output: 321
#
# Example 2:
# ----------
# Input: x = -123
# Output: -321
#
# Example 3:
# ----------
# Input: x = 120
# Output: 21
#
# Example 4:
# ------------
# Input: x = 0
# Output: 0
#
# --------
# Solution
# --------

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        real_num = abs(x)
        string = str(x)
        test_num = 0
        rev_str = 0

        while real_num > 0:
            remainder = real_num % 10
            test_num = (test_num * 10) + remainder
            real_num = real_num // 10

            if (string[0]) == '-':
                rev_str = '-' + str(test_num)
            else:
                rev_str = test_num

            if test_num < -2147483648 or test_num > 2147483647:
                rev_str = 0

        return rev_str


p1 = Solution()
print(p1.reverse(321))

