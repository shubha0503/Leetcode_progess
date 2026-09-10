# Last updated: 9/10/2026, 1:50:36 PM
1class Solution:
2    def averageOfSubtree(self, root: TreeNode) -> int:
3        def dfs(root) -> tuple:
4            if not root:
5                return 0, 0
6            ls, ln = dfs(root.left)
7            rs, rn = dfs(root.right)
8            s = ls + rs + root.val
9            n = ln + rn + 1
10            nonlocal ans
11            ans += int(s // n == root.val)
12            return s, n
13
14        ans = 0
15        dfs(root)
16        return ans