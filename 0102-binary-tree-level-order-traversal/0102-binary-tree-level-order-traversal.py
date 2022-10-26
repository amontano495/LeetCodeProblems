# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
            if root is None:
                return []
            queue = deque([root])
            ans = []
            
            while queue:
                level = []
                for i in range(len(queue)):
                    tmp = queue.popleft()
                    level.append(tmp.val)
                    if tmp.left is not None:
                        queue.append(tmp.left)
                    if tmp.right is not None:
                        queue.append(tmp.right)
                ans.append(level)
            return ans