# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node:Optional[TreeNode], maxValue):
            nonlocal count
            if not node:
                return 0
            
            if node.val >= maxValue:
                count += 1
            
            maxValue = max(maxValue, node.val) 
            
            left = dfs(node.left, maxValue) 
            right = dfs(node.right, maxValue)
        
        dfs(root, root.val)            
        return count 
