# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        invertedLeft = self.invertTree(root.left)
        return self.sameTree(invertedLeft,root.right)
        
    def invertTree(self, root):
        if root is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
            
        return root
            
    def sameTree(self,a,b):
        if a is None and b is None:
            return True
        
        if a is not None and b is not None:
            return self.sameTree(a.left,b.left) and self.sameTree(a.right,b.right) and a.val == b.val
        
        return False
        