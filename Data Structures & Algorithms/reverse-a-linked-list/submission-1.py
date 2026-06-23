# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None 
        curr = head 

        while curr:
            tex = curr.next
            curr.next = res

            res = curr
            curr = tex
        return res