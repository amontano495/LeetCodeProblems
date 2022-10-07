# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import math
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = head
        count = 0
        while(tmp.next is not None):
            tmp = tmp.next
            count += 1
        
        tmp = head
        i = 0
        while(i < math.ceil(count/2)):
            tmp = tmp.next
            i += 1
        
        return tmp