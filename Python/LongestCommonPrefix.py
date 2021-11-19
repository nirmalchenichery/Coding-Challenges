# ---------------
# Longest Common Prefix
# ---------------
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# --------
# Solution
# --------

class Solution(object):
    def longestCommonPrefix(self, strs) -> str:
        result = ""
        # take arbitrary string for iteration
        for i in range(len(strs[0])):
            #check each element in the List
            for s in strs:
                #check first string - first element
                # not equal to list string first element
                if i == len(s) or s[i] != strs[0][i]:
                    return result
            result += strs[0][i]

        return result

# input_list = ["dog","racecar","car"]
input_list = ["flower","flow","flight"]
# input_list = [""]
# input_list = [""]
# input_list = ["a"]

p1 = Solution()
print(p1.longestCommonPrefix(input_list))

