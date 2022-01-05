# ----------------------------
# 58. Length of Last Word
# ----------------------------

# Given a string s consisting of some words separated by some number of spaces,
# return the length of the last word in the string.
#
# A word is a maximal substring consisting of non-space characters only.
#
# Example 1:
# ----------
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
#
# Example 2:
# ---------
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
#
# Example 3:
# ---------
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


# ---------
# Solution
# ---------

class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        strlist = s.split()
        return (len(strlist[-1]))


s = "Hello World"
p1 = Solution()
print(p1.lengthOfLastWord(s))
#
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         n = 0
#         i = len(s)-1
#         while i >=0:
#             if s[i] != " ":
#                 n += 1
#             elif n > 0 and s[i] == " ":
#                 return n
#             i -= 1
#         return n

