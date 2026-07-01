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
            return None

        #create node
        curr = head 
        while curr:
            copy[curr] = Node(curr.val)            
            curr = curr.next
        
        #put the value 
        curr = head 
        while curr:
            newNode = copy[curr]
            
            #combine next
            if curr.next:
                newNode.next = copy[curr.next]
            else:
                newNode.next = None
            
            #combine random            
            if curr.random:
                newNode.random = copy[curr.random]
            else:
                newNode.random = None
            
            curr = curr.next
        
        return copy[head] 