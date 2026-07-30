# Last updated: 7/30/2026, 5:20:58 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        n = len(word)
4        ans, k = 0, 1
5        for _ in range(n // 8):
6            ans += k * 8
7            k += 1
8        ans += k * (n % 8)
9        return ans