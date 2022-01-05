# ----------------------------
# Min Window Substring
# ----------------------------

# Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr,
# which will contain only two strings, the first parameter being the string N and
# the second parameter being a string K of some characters, and your goal is to determine the smallest
# substring of N that contains all the characters in K. For example: if strArr is ["aaabaaddae", "aed"]
# then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string.
# So for this example your program should return the string dae.
#
# Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of
# the characters in K is "aabd" which is located at the beginning of the string. Both parameters will be strings
# ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N.
# Both strings will only contains lowercase alphabetic characters.

# Examples
# ---------
# Input: ["ahffaksfajeeubsne", "jefaa"]
# Output: aksfaje
#
# Input: ["aaffhkksemckelloe", "fhea"]
# Output: affhkkse


# ---------
# Solution
# ---------
def MinWindowSubstring(strArr):
    s = strArr[0]
    t = strArr[1]

    if t == "": return ""

    countT, window = {}, {}
    for c in t:
        countT[c] = 1 + countT.get(c, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1

        while have == need:
            # update our result
            if (r - l + 1) < resLen:
                res = [l, r]
                resLen = (r - l + 1)
            # pop from the left of our window
            window[s[l]] -= 1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have -= 1
            l += 1
    l, r = res
    return s[l:r + 1] if resLen != float("infinity") else ""


arr =  ["aaffhkksemckelloe", "fhea"]
# keep this function call here
print(MinWindowSubstring(arr))