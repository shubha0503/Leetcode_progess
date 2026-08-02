# Last updated: 8/2/2026, 11:16:16 AM
class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        ans = 0
        for i, x in enumerate(sorted(cnt.values(), reverse=True)):
            ans += (i // 8 + 1) * x
        return ans