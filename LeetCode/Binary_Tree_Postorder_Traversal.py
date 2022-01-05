'''
--------------------------------------
145. Binary Tree Postorder Traversal
--------------------------------------
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:
-----------
    1
      \
        2
       /
     3

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
----------
Input: root = []
Output: []

Example 3:
----------
Input: root = [1]
Output: [1]

Example 4:
----------
         1
        /
      2

Input: root = [1,2]
Output: [2,1]

Example 5:
-----------
    1
     \
      2

Input: root = [1,null,2]
Output: [2,1]

Constraints:

The number of the nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?

'''

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        result = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            temp = stack[-1].right
            if temp:
                root = temp
            else:
                temp = stack.pop()
                result.append(temp.val)
                while stack and temp == stack[-1].right:
                    temp = stack.pop()
                    result.append(temp.val)
        return result
