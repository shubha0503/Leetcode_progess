# Last updated: 7/11/2026, 11:55:37 AM
1class Solution:
2    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
3        def dfs(i: int) -> (int, int):
4            vis[i] = True
5            x, y = 1, len(g[i])
6            for j in g[i]:
7                if not vis[j]:
8                    a, b = dfs(j)
9                    x += a
10                    y += b
11            return x, y
12
13        g = defaultdict(list)
14        for a, b in edges:
15            g[a].append(b)
16            g[b].append(a)
17        vis = [False] * n
18        ans = 0
19        for i in range(n):
20            if not vis[i]:
21                a, b = dfs(i)
22                ans += a * (a - 1) == b
23        return ans
24        