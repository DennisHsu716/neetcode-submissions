# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = slow = fast = head 
        res = None 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next 
        slow.next = None

        while second:
            nex = second.next 
            second.next = res 

            res = second
            second = nex 
        
        while first and res:
            imp1 = first.next
            imp2 = res.next 

            first.next = res 
            res.next = imp1

            first = imp1
            res = imp2