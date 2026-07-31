# Last updated: 7/31/2026, 11:28:34 PM
1class Solution:
2    def minimumPushes(self, word: str) -> int:
3        cnt = Counter(word)
4        ans = 0
5        for i, x in enumerate(sorted(cnt.values(), reverse=True)):
6            ans += (i // 8 + 1) * x
7        return ans