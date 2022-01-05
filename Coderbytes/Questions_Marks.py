'''

----------------------------
  Questions Marks
----------------------------

Have the function QuestionsMarks(str) take the str string parameter, which will contain single digit numbers, letters,
and question marks, and check if there are exactly 3 question marks between every pair of two numbers that add up to 10.
If so, then your program should return the string true, otherwise it should return the string false.
If there aren't any two numbers that add up to 10 in the string, then your program should return false as well.

For example: if str is "arrb6???4xxbl5???eee5" then your program should return true because there are exactly 3
question marks between 6 and 4, and 3 question marks between 5 and 5 at the end of the string.


Examples
----------
Input: "aa6?9"
Output: false

Input: "acc?7??sss?3rr1??????5"
Output: true

# 1. For input "aaaaaaarrrrr??????" the output was incorrect. The correct output is false
# 2. For input "9???1???9??1???9" the output was incorrect. The correct output is false

---------
Solution
---------

'''

def QuestionsMarks(strParam):
    lastDigit = None
    result = False
    for i in range(len(strParam)):
      if strParam[i].isdigit():
        if lastDigit:
          if int(strParam[i]) + int(strParam[lastDigit]) == 10:
             if strParam[lastDigit:i].count('?') == 3:
               result = True
             else:
               result = False
          else:
            result = False

        lastDigit = i
      # else:
      #   result = False

      return result

#
# def QuestionsMarks2(str):
#   a = 11
#   b = 'false'
#   c = 0
#   for i in str:
#     if i.isdigit():
#       if int(i) + a == 10:
#         if c != 3:
#           return 'false'
#           b = 'true'
#       c = 0
#       a = int(i)
#
#     elif i == '?':
#         c += 1
    return b

# strParam = "aa6?9"
# # Output: false -- OK
#
strParam = "acc?7??sss?3rr1??????5"
# # Output: true -- Wrong
#

# strParam = "aaaaaaarrrrr??????"
# Output: false -- OK

# strParam = "9???1???9??1???9" -
# Output: false - Not sure about the result

print(QuestionsMarks(strParam))




