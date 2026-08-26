# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index = {}
        for i, val in enumerate(inorder):
            inorder_index[val] = i
        
        preorder_index = 0
        def dfs(leftindex, rightindex):
            nonlocal preorder_index
            if leftindex > rightindex:
                return None
            
            rootVal = preorder[preorder_index]
            preorder_index += 1

            root = TreeNode(rootVal)
            mid = inorder_index[rootVal]

            root.left = dfs(leftindex, mid - 1)
            root.right = dfs(mid + 1, rightindex)
        
            return root
        return dfs(0, len(inorder) - 1)