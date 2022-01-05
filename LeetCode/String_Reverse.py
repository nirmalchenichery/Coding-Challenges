
class Solution(object):

    def reverse(self, x):
        newstr = str(x)
        rev_str = ""
        for i in newstr:
            rev_str = i + rev_str

        return (rev_str)


p1 = Solution()
print(p1.reverse('-123'))
