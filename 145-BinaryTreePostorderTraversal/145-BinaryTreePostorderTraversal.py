# Last updated: 7/4/2026, 10:44:37 AM
class Solution:
    def postorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            
            dfs(node.left)     # LEFT
            dfs(node.right)    # RIGHT
            result.append(node.val)  # ROOT
        
        dfs(root)
        return result