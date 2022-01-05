'''
---------------
Bracket Matcher
---------------
Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets are correctly
matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))",
then the output should be 1, but if str is "((hello (world))" the the output should be 0 because
the brackets do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

Examples
-----------------
Input: "(coder)(byte))"
Output: 0

Input: "(c(oder)) b(yte)"
Output: 1

Test Case
----------
1. For input "hello()" the output was incorrect. The correct output is 1
2. For input "one(bracket)" the output was incorrect. The correct output is 1
3. For input "()coderbyte() yes()" the output was incorrect. The correct output is 1
4. For input "dogs and cats" the output was incorrect. The correct output is 1
5. For input "01()01()01()" the output was incorrect. The correct output is 1
6. For input "three let(t)ers" the output was incorrect. The correct output is 1
7. For input "twice thri(c)(e)()()" the output was incorrect. The correct output is 1

'''

def BracketMatcher(strParam):
    stack = []

    for strvalue in strParam:
        if strvalue == '(':
            stack.append(setattr)

        if strvalue == ')':
            if not stack:
                return 0
            else:
                stack.pop()

    return 1 if len(stack) == 0 else 0


strParam = "(coder)(byte))"
print(BracketMatcher(strParam))
