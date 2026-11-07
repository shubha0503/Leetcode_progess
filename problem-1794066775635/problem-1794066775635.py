# Last updated: 11/7/2026, 9:22:55 PM
1class Solution:
2    def canRemoveAll(self, types: list[int], colors: list[int], groupSize: list[int]) -> bool:
3        a = types, colors, groupSize
4
5        s = []
6
7        for t, c in zip(types, colors):
8
9            if s and s[-1][0] == t and s[-1][1] == c:
10                s[-1][2] += 1
11            else:
12                s.append([t, c, 1])
13
14            if s[-1][2] == groupSize[t]:
15                s.pop()
16
17        return len(s) == 0
18        