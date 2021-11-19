# ---------------
# Valid Parentheses
# ---------------

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 
# Example 1:
# --------
# Input: s = "()"
# Output: true

# Example 2:
# --------
# Input: s = "()[]{}"
# Output: true

# Example 3:
# --------
# Input: s = "(]"
# Output: false

# Example 4:
# --------
# Input: s = "([)]"
# Output: false

# Example 5:
# --------
# Input: s = "{[]}"
# Output: true

# --------
# Solution
# --------

class Solution(object):
    def isValid(self, s: str) -> bool:
        stack = []
        array_map_close_to_open = {")": "(", "]": "[", "}": "{"}

        for i in s:
            if i in array_map_close_to_open:

                if stack and stack[-1] == array_map_close_to_open[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False


# validate_input = "()"
# validate_input ="()[]{}"
# validate_input = "(]"
# validate_input ="([)]"
validate_input ="{[]}"

p1 = Solution()
print(p1.isValid(validate_input))

