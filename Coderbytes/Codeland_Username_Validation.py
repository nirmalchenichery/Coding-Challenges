# ----------------------------
# Codeland Username Validation
# ----------------------------
# Have the function CodelandUsernameValidation(str) take the str parameter being passed and determine
# if the string is a valid username according to the following rules:
#
# 1. The username is between 4 and 25 characters.
# 2. It must start with a letter.
# 3. It can only contain letters, numbers, and the underscore character.
# 4. It cannot end with an underscore character.
#
# If the username is valid then your program should return the string true, otherwise return the string false.
#
# Examples 1
# ----------
# Input: "aa_"
# Output: false
#
# Examples 2
# ----------
# Input: "u__hello_world123"
# Output: true

# ---------
# Solution
# ---------
import re

def CodelandUsernameValidation(strParam):
    pattern = "^[A-Za-z0-9_-]*$"

    if (len(strParam) < 4 or len(strParam) > 25):
        return False
    elif (not strParam[0].isalpha()):
        return False
    elif (strParam[-1] == '_' ):
        return False
    elif (bool(re.match(pattern, strParam))) == False:
        return False

    return True


# strParam = "u__hello_world123$"
strParam = "aa_a."

print(CodelandUsernameValidation(strParam))