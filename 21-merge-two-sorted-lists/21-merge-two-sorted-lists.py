# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2
        if n1 is None:
            return n2
        if n2 is None:
            return n1
        
        if n1.val < n2.val:
            n3 = ListNode(n1.val, None)
            n1 = n1.next
        else:
            n3 = ListNode(n2.val, None)
            n2 = n2.next
            
        tmp = n3
        
        while True:
            if n1 is None and n2 is None:
                break
            elif n1 is None and n2 is not None:
                val = n2.val
                n2 = n2.next
            elif n2 is None and n1 is not None:
                val = n1.val
                n1 = n1.next
            elif n1.val <= n2.val:
                val = n1.val
                n1 = n1.next
            elif n1.val > n2.val:
                val = n2.val
                n2 = n2.next
                
            tmp.next = ListNode(val,None)
            tmp = tmp.next
            
        return n3