# ----------------------------
# Bracket Combinations
# ----------------------------

# Have the function BracketCombinations(num) read num which will be an integer greater than or equal to zero,
# and return the number of valid combinations that can be formed with num pairs of parentheses.
#
# For example, if the input is 3, then the possible combinations of 3 pairs of parenthesis,
# namely: ()()(), are ()()(), ()(()), (())(), ((())), and (()()). There are 5 total combinations
# when the input is 3, so your program should return 5.

# Example 1
# ----------
# Input: 3
# Output: 5
#
# Example 2
# ----------
# Input: 2
# Output: 2

# ---------
# Solution
# ---------

from math import factorial
def BracketCombinations(num):
  num = int(factorial(2 * num) / (factorial(num + 1) * factorial(num)))
  return int(num)

# keep this function call here
print(BracketCombinations(3))
