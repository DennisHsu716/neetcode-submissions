# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy 
        res = []
        carry = 0

        
        while l1 or l2 or carry:
        #find the l1 and l2
            if l1:
                val1 = l1.val 
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0
        #combine l1 and l2 and carry
            total = val1 + val2 + carry
        #move carry
            carry = total // 10
            digit = total % 10

        #move tail
            tail.next  = ListNode(digit) 

            tail = tail.next 

            if l1:
                l1 = l1.next 
            else:
                l1 = None 
            
            if l2:
                l2 = l2.next 
            else:
                l2 = None 
        
        return dummy.next 