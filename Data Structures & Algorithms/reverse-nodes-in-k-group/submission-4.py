# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy =ListNode()
        dummy.next = head
        grepPrev = dummy

        while True:
            curr = grepPrev
            for i in range(k):
                curr = curr.next
                if curr == None:
                    return dummy.next 
            
            grepNext = curr.next 
            tmp = curr = grepPrev.next
            prev = grepNext 

            while curr != grepNext:
                nex = curr.next 
                curr.next = prev 

                prev = curr
                curr = nex 

            grepPrev.next = prev
            grepPrev = tmp
        return dummy.next