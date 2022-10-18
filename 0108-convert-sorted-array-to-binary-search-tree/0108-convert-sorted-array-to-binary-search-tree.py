# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.insertBST(nums, 0, len(nums)-1)
        
    def insertBST(self, nums, l, r):
        if(l > r):
            return None
        
        mid = int((l + r) / 2)
        BST = TreeNode(nums[mid])
        BST.left = self.insertBST(nums,l, mid-1)
        BST.right = self.insertBST(nums,mid+1,r)
        return BST
    
    