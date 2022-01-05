# -----------------------
# Merge Two Sorted Lists
# -----------------------
# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.
#
# Example 3:
# # ---------
# Input: l1 = [1,2,4], l2 = [1,3,4]
# Output: [1,1,2,3,4,4]
#
# Example 2:
# # ----------
# Input: l1 = [], l2 = []
# Output: []
#
# Example 3:
# # ----------
# Input: l1 = [], l2 = [0]
# Output: [0]

# ---------
# Solution
# ---------
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummyNode = ListNode()
        tailNode = dummyNode
        list1 = l1
        list2 = l2

        while list1 and list2:
            if list1.val < list2.val:
                tailNode.next = list1
                list1 = list1.next
            else:
                tailNode.next = list2
                list2 = list2.next

            tailNode = tailNode.next

        if list1:
            tailNode.next = list1
        else:
            tailNode.next = list2

        return dummyNode.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]

p1 = Solution()
print(p1.mergeTwoLists(l1, l2))