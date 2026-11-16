# Last updated: 11/16/2026, 9:21:48 PM
1
2class Solution:
3    def digitSum(self, s: str, k: int) -> str:
4
5        while len(s) > k:
6            new_s = ""
7
8            for i in range(0, len(s), k):
9                group = s[i:i+k]
10
11                total = sum(int(ch) for ch in group)
12
13                new_s += str(total)
14
15            s = new_s
16
17        return s
18