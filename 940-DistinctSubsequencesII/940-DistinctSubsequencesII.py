# Last updated: 9/10/2026, 1:54:16 PM
1class Solution:
2    def distinctSubseqII(self, s: str) -> int:
3        mod = 10**9 + 7
4        f = [0] * 26
5        for c in s:
6            f[ord(c) - ord("a")] = (sum(f) + 1) % mod
7        return sum(f) % mod