# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = fast = slow = head 
        res = None 

        #find the end 
        while fast and fast.next:
            fast = fast.next.next 
            slow = slow.next 
        
        second = slow.next
        slow.next = None

        #cut to half
        while second:
            nex = second.next 
            second.next = res
            res = second
            second = nex

        #switch  
        while first and res:
            tmp1 = first.next 
            tmp2 = res.next 

            first.next = res  
            res.next = tmp1

            first = tmp1 
            res = tmp2