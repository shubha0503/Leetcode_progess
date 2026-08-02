# Last updated: 8/2/2026, 11:16:19 AM
class Solution:
    def minimumPushes(self, word: str) -> int:
        n = len(word)
        ans, k = 0, 1
        for _ in range(n // 8):
            ans += k * 8
            k += 1
        ans += k * (n % 8)
        return ans