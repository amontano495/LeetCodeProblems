# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is not None:
            if self.equivTree(root,subRoot):
                return True
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        
    def equivTree(self, p, q):
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        return p.val == q.val and self.equivTree(p.left, q.left) and self.equivTree(p.right,q.right)