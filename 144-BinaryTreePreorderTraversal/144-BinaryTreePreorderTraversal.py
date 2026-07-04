# Last updated: 7/4/2026, 10:44:39 AM
class Solution:
    def preorderTraversal(self, root):
        result = []
        
        def dfs(node):
            if not node:
                return
            
            result.append(node.val)   # ROOT
            dfs(node.left)            # LEFT
            dfs(node.right)           # RIGHT
        
        dfs(root)
        return result