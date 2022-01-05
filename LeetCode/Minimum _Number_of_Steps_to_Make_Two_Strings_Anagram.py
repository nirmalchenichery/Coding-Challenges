'''
----------------------------------------------------------
1347. Minimum Number of Steps to Make Two Strings Anagram
----------------------------------------------------------

You are given two strings of the same length s and t. In one step you can choose any character of t and replace it with
another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

 Example 1:

Input: s = "bab", t = "aba"
Output: 1

Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.

Example 2:

Input: s = "leetcode", t = "practice"
Output: 5

Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

Example 3:

Input: s = "anagram", t = "mangaar"
Output: 0

Explanation: "anagram" and "mangaar" are anagrams.

Constraints:

1 <= s.length <= 5 * 104
s.length == t.length
s and t consist of lowercase English letters only.

'''
from collections import Counter
class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        return sum(list(dict(Counter(s) - Counter(t)).values()))

    def minStepsUsingArray(self,s,t):
        sCounter = {}
        tCounter = {}

        for i in s:
            if i in sCounter:
                sCounter[i] += 1
            else:
                sCounter[i] = 1

        for i in t:
            if i in tCounter:
                tCounter[i] += 1
            else:
                tCounter[i] = 1

        steps = 0
        for i in sCounter:

            si = sCounter.get(i, 0) - tCounter.get(i, 0)
            if si > 0:
                steps += si

        return steps


p1 = Solution()
s = 'leetcode'
t = 'practice'
print(p1.minSteps(s, t))
print(p1.minStepsUsingArray(s, t))

