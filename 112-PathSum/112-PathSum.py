# Last updated: 7/4/2026, 10:44:54 AM
class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        
        # If it's a leaf node, check sum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Check left or right subtree
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
