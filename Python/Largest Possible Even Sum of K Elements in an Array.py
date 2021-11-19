# ---------------------------------------------------------------------
# Find the largest possible sum of K element at different positions in A
# ---------------------------------------------------------------------
# You are given an array A og N positive integer and an integer K.
# Find the largest possible sum of K element at different positions in A
#
# For example given A = [4,9,8,2,6] and K=3, the largest even sum of three elements is 18.
# the three selected elements are A[0] = 4, A[2] = 8, A[4] = 6
#
# if there are no such elements, return -1

class Solution:
    def findLargestEven(self, a , k):
        odd = []
        even = []
        evenSum = 0
        h = -1

        if len(a) < k:
            return -1

        # Creating Odd and Even number from the List
        for i in a:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        # Sort
        even.sort()
        odd.sort()

        if len(even) == 0:
            return -1

        if len(even) > k:
            for j in range(k, 0, -1):
                evenSum += even[j]
        else:
            # Sum of all even
            for even_value in even:
                evenSum += even_value
            # remaining values from original array
            index_for_remaining = abs(k - len(even))
            for loop_cnt in range(index_for_remaining):
                evenSum += odd[h]
                h += -1

        return evenSum


p1 = Solution()

A = [4,9,8,2,6]
K = 3

# A = [5,6,3,4,2]
# K = 5

# A = [7,7,7,7,7,7]
# K = 1

# A = [100000]
# K = 2

print(p1.findLargestEven(A,  K))