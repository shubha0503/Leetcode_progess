# Last updated: 7/4/2026, 10:44:56 AM
class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        
        # If one child is missing, take the other
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        
        # Both children exist
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))