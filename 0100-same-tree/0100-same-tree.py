# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is not None and q is not None:
            l_same = self.isSameTree(p.left,q.left)
            r_same = self.isSameTree(p.right,q.right)
            return p.val == q.val and l_same and r_same
        if p is None and q is None:
            return True
        return False