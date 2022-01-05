# ---------------
# Number Encoding
# ---------------

# Using the JavaScript language, have the function NumberEncoding(str) take the str parameter and
# encode the message according to the following rule:
#
# encode every letter into its corresponding numbered position in the alphabet.
# Symbols and spaces will also be used in the input. For example: if str is "af5c a#!"
# then your program should return 1653 1#!.

# Example 1
# ------------
# Input = "hello 45"
# Output = 85121215 45
#
# Example 2
# ------------
# Input = "jaj-a"
# Output = 10110-1

# --------
# Solution
# --------

class Solution(object):
    def numberEncoding(self, strvalue):
        newStrlist = []
        newStr = ''

        for i in range(len(strvalue)):
            if ((strvalue[i] >= 'a' and strvalue[i] <= 'z') or (strvalue[i] >= 'A' and strvalue[i] <= 'Z')):
                newStrlist.append(ord(strvalue[i]) - 96)
            else:
                newStrlist.append(strvalue[i])

        for index in newStrlist:
           newStr = (newStr) + str(index)

        return newStr


strvalue = "jaj-a"
# strvalue = "hello 45"
p1 = Solution()
print(p1.numberEncoding(strvalue))

