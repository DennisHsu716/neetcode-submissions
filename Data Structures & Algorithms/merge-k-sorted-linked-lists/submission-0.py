# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for head in lists:
            while head:
                res.append(head.val)
                head = head.next
        
        res.sort()

        dummy = ListNode()
        tail = dummy 

        for i in res:
            tail.next = ListNode(i)
            tail = tail.next
        return dummy.next