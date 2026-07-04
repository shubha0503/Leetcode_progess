# Last updated: 7/4/2026, 10:44:05 AM
class Solution:
    def sumRootToLeaf(self, root):
        def dfs(node, current):
            if not node:
                return 0
            
            # Form binary number
            current = current * 2 + node.val
            
            # If leaf node
            if not node.left and not node.right:
                return current
            
            # Recur left + right
            return dfs(node.left, current) + dfs(node.right, current)
        
        return dfs(root, 0)