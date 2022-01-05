'''
-----------------------------------
144. Binary Tree Preorder Traversal
------------------------------------

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example 1:
-----------
    1
      \
        2
       /
      3

Input: root = [1, null, 2, 3]
Output: [1, 2, 3]

Example 2:
----------
Input: root = []
Output: []

Example 3:
----------
Input: root = [1]
Output: [1]

Example 4:
-----------
     1
    /
  2

Input: root = [1, 2]
Output: [1, 2]

Example 5:
-----------
  1
    \
      2

Input: root = [1, null, 2]
Output: [1, 2]

Constraints:

The number of nodes in the tree is in the range[0, 100].

-100 <= Node.val <= 100

Follow
up: Recursive solution is trivial, could you do it iteratively?

'''

class Solution:
    # Recursive

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    # Iterative
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        stack = [root]
        result = []
        while stack != []:
            root = stack.pop()
            result.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

        return result


