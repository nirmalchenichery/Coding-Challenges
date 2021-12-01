# ----------------------------
# 83. Remove Duplicates from Sorted Lis
# ----------------------------
# Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
# Return the linked list sorted as well.

# Example 1:
# -----------
# Input: head = [1,1,2]
# Output: [1,2]
#
# Example 2:
# -----------
# Input: head = [1,1,2,3,3]
# Output: [1,2,3]


# ---------
# Solution
# ---------
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        curNode = head

        while curNode:
            while curNode.next and curNode.next.val == curNode.val:
                curNode.next = curNode.next.next

            curNode = curNode.next

        return head


head = [1, 1, 2, 3, 3]

p1 = Solution()
print(p1.deleteDuplicates(head))

