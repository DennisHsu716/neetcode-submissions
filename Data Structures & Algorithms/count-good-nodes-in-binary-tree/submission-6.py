# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        
        def dfs(node:Optional[TreeNode], max_node):
            nonlocal count
            if not node:
                return 0

            if node.val >= max_node:
                count += 1
            max_node = max(max_node, node.val)

            left = dfs(node.left, max_node)
            right = dfs(node.right, max_node)
        
        dfs(root, root.val)
        return count 