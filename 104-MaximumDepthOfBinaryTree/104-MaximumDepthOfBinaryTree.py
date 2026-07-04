# Last updated: 7/4/2026, 10:45:04 AM
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        return 1 + max(left_depth, right_depth)