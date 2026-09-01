# Last updated: 9/1/2026, 11:08:08 AM
1class Solution:
2    def minMoves(self, classroom: List[str], energy: int) -> int:
3        m, n = len(classroom), len(classroom[0])
4        d = [[0] * n for _ in range(m)]
5        x = y = cnt = 0
6        for i, row in enumerate(classroom):
7            for j, c in enumerate(row):
8                if c == "S":
9                    x, y = i, j
10                elif c == "L":
11                    d[i][j] = cnt
12                    cnt += 1
13        if cnt == 0:
14            return 0
15        vis = [
16            [[[False] * (1 << cnt) for _ in range(energy + 1)] for _ in range(n)]
17            for _ in range(m)
18        ]
19        q = [(x, y, energy, (1 << cnt) - 1)]
20        vis[x][y][energy][(1 << cnt) - 1] = True
21        dirs = (-1, 0, 1, 0, -1)
22        ans = 0
23        while q:
24            t = q
25            q = []
26            for i, j, cur_energy, mask in t:
27                if mask == 0:
28                    return ans
29                if cur_energy <= 0:
30                    continue
31                for k in range(4):
32                    x, y = i + dirs[k], j + dirs[k + 1]
33                    if 0 <= x < m and 0 <= y < n and classroom[x][y] != "X":
34                        nxt_energy = (
35                            energy if classroom[x][y] == "R" else cur_energy - 1
36                        )
37                        nxt_mask = mask
38                        if classroom[x][y] == "L":
39                            nxt_mask &= ~(1 << d[x][y])
40                        if not vis[x][y][nxt_energy][nxt_mask]:
41                            vis[x][y][nxt_energy][nxt_mask] = True
42                            q.append((x, y, nxt_energy, nxt_mask))
43            ans += 1
44        return -1