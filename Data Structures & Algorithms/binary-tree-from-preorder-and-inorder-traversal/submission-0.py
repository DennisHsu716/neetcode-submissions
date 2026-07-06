# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inordermap = {}

        for i, val in enumerate(inorder):
            inordermap[val] = i
        
        preindex = 0
        def dfs(leftindex, rightindex):
            nonlocal preindex 

            if leftindex > rightindex:
                return None 
            
            rootVal = preorder[preindex]
            preindex += 1

            root = TreeNode(rootVal) 

            mid = inordermap[rootVal]

            root.left = dfs(leftindex, mid - 1) 

            root.right = dfs(mid + 1, rightindex)

            return root 
        return dfs(0, len(inorder) - 1) 
