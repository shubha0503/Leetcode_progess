# Last updated: 7/17/2026, 11:07:28 PM
1class Solution:
2    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
3        mx = max(nums)
4        cnt = Counter(nums)
5        cnt_g = [0] * (mx + 1)
6        for i in range(mx, 0, -1):
7            v = 0
8            for j in range(i, mx + 1, i):
9                v += cnt[j]
10                cnt_g[i] -= cnt_g[j]
11            cnt_g[i] += v * (v - 1) // 2
12        s = list(accumulate(cnt_g))
13        return [bisect_right(s, q) for q in queries]