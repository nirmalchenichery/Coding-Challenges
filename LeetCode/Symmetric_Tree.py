'''
------------------------------------
101. Symmetric Tree
------------------------------------
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:

    1
   / \
  2   2
 / \ / \
3  4 4  3


Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:

    1
   / \
  2   2
   \   \
   3    3

Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?


'''

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return true

        return self.isMirror(root.left, root.right)

    def isMirror(self, leftroot, rightroot):
        if leftroot and rightroot:
            return leftroot.val == rightroot.val and self.isMirror(leftroot.left, rightroot.right) and self.isMirror(
                leftroot.right, rightroot.left)
        return leftroot == rightroot

