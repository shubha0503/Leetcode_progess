# Last updated: 7/4/2026, 10:45:08 AM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        # If both nodes are None → trees match at this branch
        if not p and not q:
            return True
        
        # If one exists and other doesn't → not same
        if not p or not q:
            return False
        
        # Values must match AND left subtree must match AND right subtree must match
        return (p.val == q.val 
                and self.isSameTree(p.left, q.left) 
                and self.isSameTree(p.right, q.right))