# Last updated: 11/6/2026, 10:37:15 PM
1class Solution:
2    def countServers(self, n, logs, x, queries):
3
4        logs.sort(key=lambda a: a[1])
5
6        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
7
8        count = {}
9        ans = [0] * len(queries)
10
11        left = 0
12        right = 0
13
14        for q, idx in sorted_queries:
15
16            # Add new logs
17            while right < len(logs) and logs[right][1] <= q:
18                server = logs[right][0]
19                count[server] = count.get(server, 0) + 1
20                right += 1
21
22            # Remove expired logs
23            while left < right and logs[left][1] < q - x:
24                server = logs[left][0]
25                count[server] -= 1
26
27                if count[server] == 0:
28                    del count[server]
29
30                left += 1
31
32            # Calculate inactive servers
33            ans[idx] = n - len(count)
34
35        return ans