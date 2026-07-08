# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node:Optional[TreeNode]):
            nonlocal res
            if not node:
                res.append("N")
                return 
            
            res.append(str(node.val))
            left = dfs(node.left)
            right = dfs(node.right)
        
        dfs(root)
        return ",".join(res) 

        
    # Decodes your encoded data to tree. 
    def deserialize(self, data: str) -> Optional[TreeNode]:
        value = data.split(",")
        index = 0 

        def dfs(node:Optional[TreeNode]):
            nonlocal value, index
            if value[index] == "N":
                index += 1
                return 
            
            rootVal = value[index]
            index += 1
            root = TreeNode(int(rootVal))

            root.left = dfs(node.left) 
            root.right = dfs(node.right)

            return root
        return dfs(root)

