# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node:Optional[TreeNode], maxNode):
            nonlocal count 
            
            if not node:
                return 0
            
            if node.val >= maxNode:
                count += 1
            
            maxNode = max(maxNode, node.val)

            left = dfs(node.left, maxNode)
            right = dfs(node.right, maxNode)

            return max(left, right) + 1
        
        dfs(root, root.val)
        return count
