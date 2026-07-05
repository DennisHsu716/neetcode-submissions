"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}

        if not head:
            return []
        
        curr = head 
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next 
        
        curr = head 
        while curr:
            newNode = copy[curr]
            
            if curr.next:
                newNode.next = copy[curr.next]
            else:
                newNode.next = None
            
            if curr.random:
                newNode.random = copy[curr.random]
            else:
                newNode.random = None 
        
            curr = curr.next 
        
        return copy[head]