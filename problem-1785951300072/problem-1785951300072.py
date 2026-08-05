# Last updated: 8/5/2026, 11:05:00 PM
1class Solution:
2    def remainingMethods(
3        self, n: int, k: int, invocations: List[List[int]]
4    ) -> List[int]:
5        def dfs(i: int):
6            suspicious[i] = True
7            for j in g[i]:
8                if not suspicious[j]:
9                    dfs(j)
10
11        def dfs2(i: int):
12            vis[i] = True
13            for j in f[i]:
14                if not vis[j]:
15                    suspicious[j] = False
16                    dfs2(j)
17
18        f = [[] for _ in range(n)]
19        g = [[] for _ in range(n)]
20        for a, b in invocations:
21            f[a].append(b)
22            f[b].append(a)
23            g[a].append(b)
24        suspicious = [False] * n
25        dfs(k)
26
27        vis = [False] * n
28        ans = []
29        for i in range(n):
30            if not suspicious[i] and not vis[i]:
31                dfs2(i)
32        return [i for i in range(n) if not suspicious[i]]