# Last updated: 7/18/2026, 9:51:32 AM
1class Solution:
2    def subsequencePairCount(self, nums: List[int]) -> int:
3        @cache
4        def dfs(i: int, j: int, k: int) -> int:
5            if i < 0:
6                return int(j == k)
7            return (
8                dfs(i - 1, j, k)
9                + dfs(i - 1, gcd(nums[i], j), k)
10                + dfs(i - 1, j, gcd(nums[i], k))
11            ) % mod
12
13        mod = 10**9 + 7
14        return (dfs(len(nums) - 1, 0, 0) - 1) % mod