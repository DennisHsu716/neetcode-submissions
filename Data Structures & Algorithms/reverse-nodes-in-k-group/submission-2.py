# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head 
        groupPrev = dummy

        while True:
            curr = groupPrev
            for i in range(k):
                curr = curr.next
                if curr == None:
                    return dummy.next 
            
            groupNext = curr.next
            tmp = curr = groupPrev.next
            prev = groupNext

            while curr != groupNext:
                nex = curr.next
                curr.next = prev

                prev = curr
                curr = nex
            
            groupPrev.next = prev  
            groupPrev = tmp
        return dummy.next