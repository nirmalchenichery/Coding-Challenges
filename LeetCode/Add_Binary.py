# ----------------------------
# 67. Add Binary
# ----------------------------
# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
# -----------
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# -----------
# Input: a = "1010", b = "1011"
# Output: "10101"

# Rule for addition
#
#     0 + 0 = 0
#     1 + 0 = 1
#     1 + 1 = 0 carry i

# ---------
# Solution
# ---------

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):

            digitA = ord(a[i]) - ord("0") if i < len(a) else 0
            digitB = ord(b[i]) - ord("0") if i < len(b) else 0

            total = digitA + digitB + carry
            char = str(total % 2)
            result = char + result
            carry = total//2

        if carry:
            result = "1" + result

        return result

    # def addBinary2(self, a: str, b: str) -> str:
    #     result = ""
    #     carry = 0
    #     a, b = a[::-1], b[::-1]
    #
    #     for i in range(max(len(a), len(b))):
    #
    #         digitA = ord(a[i]) - ord("0") if i < len(a) else 0
    #         digitB = ord(b[i]) - ord("0") if i < len(b) else 0
    #
    #         total = digitA + digitB + carry
    #         char = str(total % 2)
    #         result = char + result
    #         carry = total//2
    #
    #     if carry:
    #         result = "1" + result
    #
    #     return result


a = "11"
b = "11"

p1 = Solution()
print(p1.addBinary(a, b))