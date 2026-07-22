# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = fast = slow = head 
        res = None 

        if not head or not head.next:
            return 
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        while second:
            nex = second.next
            second.next = res 

            res = second
            second = nex
        
        while first and res:
            tmp1 = first.next
            tmp2 = res.next

            first.next = res
            res.next = tmp1

            first = tmp1
            res = tmp2

