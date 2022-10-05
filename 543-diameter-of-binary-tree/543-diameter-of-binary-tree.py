# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    visited = {}
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is not None:
            left_path = self.countPath(root.left)
            right_path = self.countPath(root.right)
            total_root_path = left_path + right_path
            
            total_left_path = self.diameterOfBinaryTree(root.left)
            total_right_path = self.diameterOfBinaryTree(root.right)
            
            return max([total_left_path,total_right_path,total_root_path])
        return 0
    
    def countPath(self,root):
        if root is not None:
            return 1 + max([self.countPath(root.left),self.countPath(root.right)])
        return 0