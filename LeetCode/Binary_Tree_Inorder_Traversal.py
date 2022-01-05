'''
--------------------------------
94. Binary Tree Inorder Traversal
--------------------------------
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
--------
    1
     \
      2
     /
    3

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
-----------

Input: root = []
Output: []

Example 3:
------------

Input: root = [1]
Output: [1]

Example 4:
-----------

     1
    /
   2

Input: root = [1,2]
Output: [2,1]

Example 5:
----------
    1
     \
      2

Input: root = [1,null,2]
Output: [1,2]
'''

# ---------
# Solution
# ---------
#  Recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)

# iterative
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while root is not None or stack != []:
            while root is not None:
                stack.append(root)
                root = root.left
            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result


