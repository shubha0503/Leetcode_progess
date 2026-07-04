# Last updated: 7/4/2026, 10:45:10 AM
class Solution:
    def inorderTraversal(self, root):
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)      # 1️⃣ go left
            result.append(node.val) # 2️⃣ visit node
            inorder(node.right)     # 3️⃣ go right

        inorder(root)
        return result
