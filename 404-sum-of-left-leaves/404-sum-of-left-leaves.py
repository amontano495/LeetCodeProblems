# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            if root.left is None and root.right is None:
                return 0
            elif root.left is None and root.right is not None:
                return self.sumOfLeftLeaves(root.right)
            elif root.left.left is None and root.left.right is None and root.right is not None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            elif root.left.left is None and root.left.right is None and root.right is None:
                return root.left.val
            elif root.left is not None and root.right is not None:
                return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            elif root.left is not None and root.right is None:
                return self.sumOfLeftLeaves(root.left)