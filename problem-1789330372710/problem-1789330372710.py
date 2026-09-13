# Last updated: 9/14/2026, 1:42:52 AM
1class Solution:
2    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
3        n = len(img1)
4        cnt = Counter()
5        for i in range(n):
6            for j in range(n):
7                if img1[i][j]:
8                    for h in range(n):
9                        for k in range(n):
10                            if img2[h][k]:
11                                cnt[(i - h, j - k)] += 1
12        return max(cnt.values()) if cnt else 0