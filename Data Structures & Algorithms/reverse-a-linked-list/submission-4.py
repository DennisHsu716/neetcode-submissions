# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        res = None

        while curr:
            nex = curr.next 
            curr.next = res 

            res = curr
            curr = nex
        return res 